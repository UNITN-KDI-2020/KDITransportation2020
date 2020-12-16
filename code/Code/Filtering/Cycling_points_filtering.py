# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 21:58:11 2020

@author: Dimo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Polygon
import os



# set working directory
print(os.getcwd())
os.chdir('C:/Users/Dimo/Desktop/unitn/Third Semester/Knowledge and data Integration/Project/KDITransportation2020')


# Load the gml files
cycling_points = gpd.read_file('dataset/Scope Definition & Inception/data/cycling_points/cycling_points.geojson')

#select attributes based on informal schema
cycling_points = cycling_points[['OBJECTID','DES_TIPO_E','DESCRIZION','geometry']]

#save the file as the geoJson

cycling_points.to_file("dataset/Informal Modeling/data/cycling_points.geojson", driver='GeoJSON')

