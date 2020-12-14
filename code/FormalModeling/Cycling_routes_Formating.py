# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 23:54:45 2020

@author: Omid Jadidi
"""


#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import os
from geopy.geocoders import Nominatim

import json
from models import Location, Address, Facility, Price, Contact, Route


#%%
if __name__ == '__main__':
    
    print(os.getcwd())
    os.chdir(os.getcwd())
    
    #%%
    print("Loading dataSet...")
    #Load the file
    stazioni = gpd.read_file('../../dataset/Informal Modeling/data/cycling_routes.geojson')
    
    print('Finished Loading dataset.')
    #%% convert to world view
    
    stazioni = stazioni.set_crs(epsg=25832,allow_override=True)
    stazioni = stazioni.to_crs(epsg=4326)
    print('Finished coverting epsg.')
    #%% Loop
    
    print('Start iterating dataset ...')
    data = []
    num = 0
    for i in stazioni.itertuples():
        geolocator = Nominatim(user_agent="me")
        tempArray = list(i.geometry.coords)
        
        RouteID = i.OBJECTID
        SpeedLimit = None
        StartingPoint = tempArray[0]
        ArrivalPoint = tempArray[-1]
        ModeOfTransport = 'Bike'
        TimeSpent = None
        FacilityB = None
        Lenghtt = i.geometry.length
        Rooute = Route('Route',RouteID,SpeedLimit,StartingPoint,ArrivalPoint,ModeOfTransport,TimeSpent,FacilityB,Lenghtt)
        data.append(Rooute.toJSON())
        num +=1
        
        if num % 10 ==0 :
            print(str(num)+' of items done:)')
            
    print('finished Iterating Dataset.')
    #%%
    # print(os.getcwd())
    
    ds_out_path = '../../dataset/Formal Modeling/data/Cycle_Routes.json'
    with open(ds_out_path, 'w') as ds_out_file:
            json.dump(data, ds_out_file)
    print('finished dumping json and saved file.')
