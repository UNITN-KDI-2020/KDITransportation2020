# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 00:30:31 2020

@author: Omid Jadidi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import os
from geopy.geocoders import Nominatim
import random
#%%

print(os.getcwd())
os.chdir(os.getcwd())

#%%

#%% generate models empty classes

#%%

Facility_path = '../../dataset/Data Integration/data/Facility.csv'
FacilityEnum_path = '../../dataset/Data Integration/data/FacilityEnum.csv'
Address_path = '../../dataset/Data Integration/data/Address.csv'
Contact_path = '../../dataset/Data Integration/data/Contact.csv'
Price_path = '../../dataset/Data Integration/data/Price.csv'
Calendar_path = '../../dataset/Data Integration/data/Calendar.csv'
Location_path = '../../dataset/Data Integration/data/Location.csv'

print('Reading datasets...')
Facility = pd.read_csv(Facility_path)
FacilityEnum = pd.read_csv(FacilityEnum_path)
Address = pd.read_csv(Address_path)
Contact = pd.read_csv(Calendar_path)
Price = pd.read_csv(Price_path)
Calendar_path = pd.read_csv(Calendar_path)
Location = pd.read_csv(Location_path)

print('Reading datasets done.')

#%%
print("Loading Station dataSet...")
    #Load the file
stazioni = gpd.read_file('../../dataset/Informal Modeling/data/stazioni.geojson')
    
print('Finished Loading dataset.')
#%% convert to world view
    
stazioni = stazioni.set_crs(epsg=25832,allow_override=True)
stazioni = stazioni.to_crs(epsg=4326)
print('Finished coverting epsg.')
#%%
newFacility = pd.DataFrame(columns=["Address","Location"])
#%%
# print(Location.last_valid_index())
# Location.loc[0 if Facility.last_valid_index() is None else Facility.last_valid_index()+1 ] = 1
newFacility.loc[5]= [0,1]

#%% Loop
#Starting point
newFacilityID = 0 if newFacility.last_valid_index() is None else newFacility.last_valid_index()+1 

print('Start iterating dataset ...')
data = []
for i in stazioni.itertuples():
    print(i.Index)
    geolocator = Nominatim(user_agent="me")
    tempLoc =''
    tempLoc += str(i.geometry.y)+','+str(i.geometry.x)
    rawData = geolocator.reverse(tempLoc)
    newFacility.loc[newFacilityID] = [[rawData.raw['address']['state'], rawData.raw['address']['city'],
                      rawData.raw['address']['road']+','+rawData.raw['address']['suburb'] if 'suburb' in rawData.raw['address'] else '',
                      rawData.raw['address']['house_number'] if 'house_number' in rawData.raw['address'] else None,
                      rawData.raw['address']['postcode'] if 'postcode' in rawData.raw['address'] else None],[rawData.latitude,rawData.longitude,None]]
    newFacilityID+=1
print('finished Iterating Dataset.')

