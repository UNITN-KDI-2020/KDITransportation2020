# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 21:36:35 2020

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
carSharing = gpd.read_file('dataset/Scope Definition & Inception/data/car_sharing/dataCycle.geojson')

#select attributes based on informal schema
carSharing = carSharing[['nomepos','via','geometry']]

#save the file as the geoJson
carSharing.to_file("dataset/Informal Modeling/data/carSharing.geojson", driver='GeoJSON')
