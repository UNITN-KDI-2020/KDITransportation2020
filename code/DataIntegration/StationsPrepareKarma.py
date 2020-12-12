# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 17:21:49 2020

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
if __name__ == '__main__':
    
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
    # newFacility = pd.DataFrame(columns=['Province','City','Street','Number','Cap'])
    
    print('Start making datasets...')
    Facility = pd.DataFrame(columns=['RouteID','Price','Contact','FacilityEnum','Address','Calendar'])
    Price =pd.DataFrame(columns=['FacilityID','TicketID','AutonomousTransportID','Cost','CurrencyType'])
    Contact = pd.DataFrame(columns=['AgencyID','FacilityID','Phone','Email','Website'])
    Address = pd.DataFrame(columns=['FacilityID','RouteID','Province','City','Street','Number','Cap','Location'])
    Location = pd.DataFrame(columns=['AddressID','StopId','Latitude','Longitude','Altitude'])
    Calendar = pd.DataFrame(columns=['FacilityID','StopTimesID','ServiceID','Monday','Tuesday','Wednesday',
                                     'Thursday','Friday','Saturday','Sunday','StartDate','EndDate','Exceptions'])
    CalendarDates = pd.DataFrame(columns=['CalendarId','ServiceId','Date','ExceptionType'])
    
    #%% Loop
    print('Start iterating dataset ...')
    
    for i in stazioni.itertuples():
        idx = i.Index
        geolocator = Nominatim(user_agent="me")
        tempLoc =''
        tempLoc += str(i.geometry.y)+','+str(i.geometry.x)
        rawData = geolocator.reverse(tempLoc)
        #set price
        Price.loc[idx] = [None,None,None,None,None]
        Contact.loc[idx]= [None,idx,None,None,None]
        Address.loc[idx] = [idx,None,rawData.raw['address']['state'],
                            rawData.raw['address']['city'],
                            rawData.raw['address']['road']+','+rawData.raw['address']['suburb'] if 'suburb' in rawData.raw['address'] else None,
                            rawData.raw['address']['house_number'] if 'house_number' in rawData.raw['address'] else None,
                            rawData.raw['address']['postcode'] if 'postcode' in rawData.raw['address'] else None,
                            idx]
        #set Location
        Location.loc[idx] = [idx,None,rawData.latitude,rawData.longitude,0]
        # location = Location(rawData.latitude,rawData.longitude,None)
        Calendar.loc[idx]= [None,None,None,None,None,None,None,None,None,None,None,None,None]
        Facility.loc[idx] = [None,idx,idx,2,idx,idx]
        # address = Address(rawData.raw['address']['state'], rawData.raw['address']['city'],
        #                   rawData.raw['address']['road']+','+rawData.raw['address']['suburb'] if 'suburb' in rawData.raw['address'] else '',
        #                   rawData.raw['address']['house_number'] if 'house_number' in rawData.raw['address'] else None,
        #                   rawData.raw['address']['postcode'] if 'postcode' in rawData.raw['address'] else None,
        #                   location)
        # contact = Contact(phone= None, email= None, website= None)
        # facility = Facility('RailwayStation', None, contact, None, address, None)
        # data.append(facility.toJSON())
    print('finished Iterating Dataset.')

  #%%
    print('Start exporting datasets...')
    exportPath = '../../dataset/Data Integration/data/Stations/'
    Facility.to_csv(exportPath+'Facility.csv')
    Price.to_csv(exportPath+'Price.csv')
    Contact.to_csv(exportPath+'Contact.csv')
    Address.to_csv(exportPath+'Address.csv')
    Location.to_csv(exportPath+'Location.csv')
    Calendar.to_csv(exportPath+'Calendar.csv')
    CalendarDates.to_csv(exportPath+'CalendarDates.csv')
    print('export done.')
    #%%