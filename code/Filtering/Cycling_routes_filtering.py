# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 22:07:30 2020

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
cycling_routes = gpd.read_file('dataset/Scope Definition & Inception/data/cycling_routes/cycling_routes.geojson')

#select attributes based on informal schema
cycling_routes = cycling_routes[['OBJECTID','geometry']]

#save the file as the geoJson

cycling_routes.to_file("dataset/Informal Modeling/data/cycling_routes.geojson", driver='GeoJSON')

