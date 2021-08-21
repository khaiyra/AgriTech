# AgriTech -  USGS LIDAR Challenge

### Overview
AgriTech is interested in how water flows through a maize field. This helps improve research on new agricultural products being tested on farms.

### Objective
This project aims to build an easy to use, reliable and well designed python module for AgriTech that domain experts and data scientists can use to fetch, visualise, and transform publicly available satellite and LIDAR (Light Detection And Ranging) data. This module can be found in the [module.py](https://github.com/khaiyra/AgriTech/blob/main/module.py) file.

### Data Overview
The United States Geological Survey (USGS) recently released high resolution elevation data as a LIDAR (Light Detection And Ranging) point cloud, a technology used to create high-resolution models of ground elevation called USGS 3DEP in a public dataset on Amazon. This dataset is essential to build models of water flow and predict plant health and maize harvest.
This data was read from the [USGS 3DEP AWS Public Dataset](https://www.usgs.gov/news/usgs-3dep-lidar-point-cloud-now-available-amazon-public-dataset) using PDAL’s (Point Data Abstraction Library) reader.ept  to fetch and manipulate point cloud LIDAR data.


### Functionalities
* Interface with USGS 3DEP and fetch data using their API
* Query the data model
* Terrain visualization
* Data transformation 