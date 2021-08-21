import json
import pdal
import traceback
import geopandas as gpd
from osgeo import gdal,ogr
import sys 
import os
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import griddata
import numpy as np
from shapely.geometry import box

class Module:
    """ """
    def create_pipeline(pipeline_path:str ,bounds:str,location:str):
        try:
            pipeline_json = json.load(open(pipeline_path))
            pipeline_json['pipeline'][0]['bounds'] = bounds
            pipeline_json['pipeline'][0]['filename'] = location
            return pipeline_json
        except Exception:
            print("Error Occured")
            traceback.print_exc()
            
    def read_data(pipeline) -> None:
        try:
            print('feeding pipeline to pdal...')
            pipeline = pdal.Pipeline(json.dumps(pipeline))
            print('Executing pipeline...')
            pipeline.execute()
            print('Execution Complete!')
        except Exception:
            print("Error Occured")
            traceback.print_exc()

    def convert_tif_to_shp(self,src_tif:str , output:str):
        # mapping between gdal type and ogr field type
        type_mapping = { gdal.GDT_Byte: ogr.OFTInteger,
        gdal.GDT_UInt16: ogr.OFTInteger,
        gdal.GDT_Int16: ogr.OFTInteger,
        gdal.GDT_UInt32: ogr.OFTInteger,
        gdal.GDT_Int32: ogr.OFTInteger,
        gdal.GDT_Float32: ogr.OFTReal,
        gdal.GDT_Float64: ogr.OFTReal,
        gdal.GDT_CInt16: ogr.OFTInteger,
        gdal.GDT_CInt32: ogr.OFTInteger,
        gdal.GDT_CFloat32: ogr.OFTReal,
        gdal.GDT_CFloat64: ogr.OFTReal}
    
        # this allows GDAL to throw Python Exceptions
        gdal.UseExceptions()
        print("reading tif file...")

        try:
            ds = gdal.Open(src_tif)
        
        except RuntimeError as e:
            print('Unable to open file')
            print(e)
            sys.exit(1)

        try:
            srcband = ds.GetRasterBand(1)
        
        except RuntimeError as e:
            # for example, try GetRasterBand(10)
            print('Band ( %i ) not found' % 1)
            print(e)
            sys.exit(1)

            # create shapefile datasource from geotiff file
            print("creating shapefile...")
            dst_layername = "Shape"
            drv = ogr.GetDriverByName("ESRI Shapefile")
            dst_ds = drv.CreateDataSource(output)
            dst_layer = dst_ds.CreateLayer(dst_layername, srs = None )
            raster_field = ogr.FieldDefn('elevation', type_mapping[srcband.DataType])
            dst_layer.CreateField(raster_field)
            gdal.Polygonize(srcband, None, dst_layer, 0, [], callback=None)
            print(f'Shapefile Completed..\nfile saved here {output}')
        
    def get_dimensions(shp_file:str) -> gpd.GeoDataFrame:  
        geo_df = gpd.read_file(shp_file)
        #change geometry to point
        geo_df['geometry'] = geo_df.geometry.centroid
        return geo_df
    
    
    def heatmap(shpfile:str, nodata_value:int = -9999)-> None:
        """
        creates heatmap of the region and its elevation
  
        """
        #read shape file 
        geo_df = gpd.read_file(shpfile)
    
        #remove no data values from data
        df = geo_df[geo_df['elevation_'] > nodata_value]
    
        plt.rcParams["figure.figsize"] = (20,10)
        fig, ax = plt.subplots(1, 1)
        df.plot(column='elevation_', cmap='OrRd', ax=ax, legend=True, legend_kwds={'label': "Elevation by point"})
        ax.legend(fontsize=15)
    
    def plot_raster(rast_data):
        """
        Plots raster tif image both in log scale(+1) and original version
        """
        fig, (axlog, axorg) = plt.subplots(1, 2, figsize=(14,7))
        im1 = axlog.imshow(np.log1p(rast_data)) # vmin=0, vmax=2.1)

        plt.title("{}".format(title), fontdict = {'fontsize': 15})  
        plt.axis('off')
        plt.colorbar(im1, fraction=0.03)