# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 18:19:01 2020

@author: Dimo
"""


import numpy as np
import pandas as pd
import xmlschema as sch
import networkx as nx
import os
from pprint import pprint
import shapefile as shp

import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Polygon


# set working directory
print(os.getcwd())
os.chdir('C:/Users/Dimo/Desktop/unitn/Third Semester/Knowledge and data Integration/Project/KDITransportation2020')


# Load the gml files
carSharing = gpd.read_file('dataset/Scope Definition & Inception/data/car_sharing/car_sharing.gml')
cycling_points = gpd.read_file('dataset/Scope Definition & Inception/data/cycling_points/elemento_puntuale.shp')
cycling_routes = gpd.read_file('dataset/Scope Definition & Inception/data/cycling_routes/elemento_ciclabile.shp')
stazioni = gpd.read_file('dataset/Scope Definition & Inception/data/stazioni/stazioni.gml')

## save to the file as geoJson
carSharing.to_file("dataset/Scope Definition & Inception/data/car_sharing/dataCycle.geojson", driver='GeoJSON')
cycling_points.to_file("dataset/Scope Definition & Inception/data/cycling_points/cycling_points.geojson", driver='GeoJSON')
cycling_routes.to_file("dataset/Scope Definition & Inception/data/cycling_routes/cycling_routes.geojson", driver='GeoJSON')
stazioni.to_file("dataset/Scope Definition & Inception/data/stazioni/stazioni.geojson", driver='GeoJSON')




# print(data['geometry'][0].x)
# world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# ax = world[world.country == 'South America'].plot(
#     color='white', edgecolor='black')
# print(world)

# base = world[world.name == 'Italy'].plot(
#     color='white', edgecolor='black')
# # base
# data.plot(marker='o', color='red', markersize=5)
# dataroutes.plot()

# dataCycle.to_file("dataCycle.geojson", driver='GeoJSON')

# dataCycle22 = gpd.read_file('dataCycle.geojson')
