# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 18:43:13 2020

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

def getLastidx(pd):
    if pd.last_valid_index() is None:
        return 0
    else:
        return pd.last_valid_index()+1


#%%
if __name__ == '__main__':

    #%%
    print("Loading dataSet...")
    #Load the file
    stazioni = gpd.read_file('../../dataset/Informal Modeling/data/cycling_routes.geojson')
    
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
    Route = pd.DataFrame(columns=['RouteID','SpeedLimit','StartingPoint','ArrivalPoint','ModeOfTransport','TimeSpent','Facility','Length'])
    ModeOfTransport = pd.DataFrame(columns=['TransportENum'])
    TimeSpent = pd.DataFrame(columns=['TimeStamp'])
    TimeStamp = pd.DataFrame(columns=['Hour','Minute','Seconds'])

    #%% Loop
    
    print('Start iterating dataset ...')
    data = []
    num = 0
    for i in stazioni.itertuples():
        idx = i.Index
        geolocator = Nominatim(user_agent="me")
        tempArray = list(i.geometry.coords)
        
        # Route.loc[i.OBJECTID] = [i.OBJECTID,1,StartingPointLocId,ArrivalPointLocId,ModeOfTransport]
        
        RouteID = i.OBJECTID
        SpeedLimit = 1
        
        StartingPoint = tempArray[0]
        StartingPointLocId = getLastidx(Location)
        Location.loc[StartingPointLocId] = [None,None,StartingPoint[1],StartingPoint[0],0]
        
        
        ArrivalPoint = tempArray[-1]
        ArrivalPointLocId = getLastidx(Location)
        Location.loc[ArrivalPointLocId] = [None,None,ArrivalPoint[1],ArrivalPoint[0],0]
        
        ModeOfTransport = 4
        
        TimeStampId = getLastidx(TimeStamp)
        TimeStamp.loc[TimeStampId] = [0,0,0]
        
        TimeSpentId = getLastidx(TimeSpent)
        TimeSpent.loc[TimeSpentId] = TimeStampId

        Lenghtt = i.geometry.length
        
        Route.loc[i.OBJECTID] = [i.OBJECTID,1,StartingPointLocId,ArrivalPointLocId,ModeOfTransport,TimeSpentId,None,Lenghtt]
        # Rooute = Route('Route',RouteID,SpeedLimit,StartingPoint,ArrivalPoint,ModeOfTransport,TimeSpent,FacilityB,Lenghtt)
        # data.append(Rooute.toJSON())
        num +=1
        
        if num % 10 ==0 :
            print(str(num)+' of items done:)')
            
    print('finished Iterating Dataset.')
    
    #%%
    print('Start exporting datasets...')
    exportPath = '../../dataset/Data Integration/data/CycleRoute/'
    Facility.to_csv(exportPath+'Facility.csv')
    Price.to_csv(exportPath+'Price.csv')
    Contact.to_csv(exportPath+'Contact.csv')
    Address.to_csv(exportPath+'Address.csv')
    Location.to_csv(exportPath+'Location.csv')
    Calendar.to_csv(exportPath+'Calendar.csv')
    CalendarDates.to_csv(exportPath+'CalendarDates.csv')
    Route.to_csv(exportPath+'Route.csv')
    # ModeOfTransport.to_csv(exportPath+'ModeOfTransport.csv')
    TimeSpent.to_csv(exportPath+'TimeSpent.csv')
    TimeStamp.to_csv(exportPath+'TimeStamp.csv')
    print('export done.')
    #%%