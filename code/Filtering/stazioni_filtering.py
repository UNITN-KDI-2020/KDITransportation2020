# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 22:12:45 2020

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
stazioni = gpd.read_file('dataset/Scope Definition & Inception/data/stazioni/stazioni.geojson')

#select attributes based on informal schema
stazioni = stazioni[['nome','geometry']]

#save the file as the geoJson

stazioni.to_file("dataset/Informal Modeling/data/stazioni.geojson", driver='GeoJSON')

