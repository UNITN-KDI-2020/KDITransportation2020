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
from models import Location, Address, Facility, Price, Contact


#%%
if __name__ == '__main__':
    
    print(os.getcwd())
    os.chdir(os.getcwd())
    
    #%%
    print("Loading dataSet...")
    #Load the file
    stazioni = gpd.read_file('../../dataset/Informal Modeling/data/carSharing.geojson')
    
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
        tempLoc =''
        tempLoc += str(i.geometry.y)+','+str(i.geometry.x)
        rawData = geolocator.reverse(tempLoc)
        location = Location(rawData.latitude,rawData.longitude,None)
        address = Address(rawData.raw['address']['state'],
                      rawData.raw['address']['city'] if 'city' in rawData.raw['address'] else None,
                      rawData.raw['address']['road'] if 'road' in rawData.raw['address'] else ''+','+rawData.raw['address']['suburb'] if 'suburb' in rawData.raw['address'] else '',
                      rawData.raw['address']['house_number'] if 'house_number' in rawData.raw['address'] else None,
                      rawData.raw['address']['postcode'] if 'postcode' in rawData.raw['address'] else None,
                      location)
        contact = Contact(phone= None, email= None, website= None)
        facility = Facility('CarSharingPark', None, contact, None, address, None)
        data.append(facility.toJSON())
        num +=1
        if num % 10 ==0 :
            print(str(num)+' of items done:)')
    print('finished Iterating Dataset.')
    #%%
    # print(os.getcwd())
    
    ds_out_path = '../../dataset/Formal Modeling/data/CarSharing.json'
    with open(ds_out_path, 'w') as ds_out_file:
            json.dump(data, ds_out_file)
    print('finished dumping json and saved file.')
