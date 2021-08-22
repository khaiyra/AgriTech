# AgriTech -  USGS LIDAR Challenge

## Overview
AgriTech is interested in how water flows through a maize field. This helps improve research on new agricultural products being tested on farms.

## Objective
This project aims to build an easy to use, reliable and well designed python module for AgriTech that domain experts and data scientists can use to fetch, visualise, and transform publicly available satellite and LIDAR (Light Detection And Ranging) data. This module can be found in the [module.py](https://github.com/khaiyra/AgriTech/blob/main/module.py) file.

## Data Overview
The United States Geological Survey (USGS) recently released high resolution elevation data as a LIDAR (Light Detection And Ranging) point cloud, a technology used to create high-resolution models of ground elevation called USGS 3DEP in a public dataset on Amazon. This dataset is essential to build models of water flow and predict plant health and maize harvest.
This data was read from the [USGS 3DEP AWS Public Dataset](https://www.usgs.gov/news/usgs-3dep-lidar-point-cloud-now-available-amazon-public-dataset) using PDAL’s (Point Data Abstraction Library) reader.ept  to fetch and manipulate point cloud LIDAR data.

## Directory Structure
* [filename.txt](https://github.com/khaiyra/AgriTech/blob/main/filename.txt): list of regions
* [iowa.json](https://github.com/khaiyra/AgriTech/blob/main/iowa.json): json pipeline file
* [iowa.tif](https://github.com/khaiyra/AgriTech/blob/main/iowa.tif): tif file of data
* [module.py](https://github.com/khaiyra/AgriTech/blob/main/module.py): python package to frtch and load data, visualize graphically the elevation in heatmap and raster image.
* [notebook.ipynb](https://github.com/khaiyra/AgriTech/blob/main/notebook.ipynb): implementaion and testing of package
* [requirements.txt](https://github.com/khaiyra/AgriTech/blob/main/requirements.txt): file for dependencies for the project

## Module Functionalities
The python package contains a class that has different python functions defined to create a PDAL pipeline, fetch and read the data, convert  the data from tif to a shp file, plot the heatmpa and raster image and also calculate and give output of its topographic wetness index(TWI) as an additional column returned with geopandas dataframe.
FUNCTIONS EXPLAINED - 
* create_pipeline: this function takes 3 aruements; the pipeline path, bound and location and returns a json pipeline that fetches the data
* read_data: reads data from the PDAL pipeline
* convert_tif_to_shp: converts tif file to shp for easier importation
* get_dimensions: returns the elevation and geometry from the shp file
* heatmap: creates heatmap of the region and its elevation
* plot_raster: plots raster tif image both in log scale(+1) and original version