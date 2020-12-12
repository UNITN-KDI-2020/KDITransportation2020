# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 01:07:34 2020

@author: Omid Jadidi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import os
#%%

print(os.getcwd())
os.chdir(os.getcwd())

# #%%
if __name__ == '__main__':
    
#     #%% generate models empty classes
#     print('Create empty files')
#     Etypes = ['Route','PublicTransport','AutonomousTransport','FuelTypeEnum','ModeOfTransport','Ticket','Agency',
#               'Facility','StopTimes','TransportEnum','Price','Contact','FacilityEnum','Address','Calendar','Stop',
#               'TimeSpent','TimeStamp','Location','CalendarDates']
#     for i in Etypes:
#         if not os.path.exists('../../dataset/Data Integration/data/'+i+'.csv'):
#             temp = pd.DataFrame()
#             path = '../../dataset/Data Integration/data/'+i+'.csv'
#             temp.to_csv(path)
#     print('Creation Done.')
    print('Start making datasets...')
    Facility = pd.DataFrame(columns=['RouteID','Price','Contact','FacilityEnum','Address','Calendar'])
    Price =pd.DataFrame(columns=['FacilityID','TicketID','AutonomousTransportID','Cost','CurrencyType'])
    Contact = pd.DataFrame(columns=['AgencyID','FacilityID','Phone','Email','Website'])
    Address = pd.DataFrame(columns=['FacilityID','RouteID','Province','City','Street','Number','Cap','Location'])
    Location = pd.DataFrame(columns=['AddressID','StopId','Latitude','Longitude','Altitude'])
    Calendar = pd.DataFrame(columns=['FacilityID','StopTimesID','ServiceID','Monday','Tuesday','Wednesday',
                                     'Thursday','Friday','Saturday','Sunday','StartDate','EndDate','Exceptions'])
    CalendarDates = pd.DataFrame(columns=['CalendarId','ServiceId','Date','ExceptionType'])
    #%%
    print('Start exporting datasets...')
    exportPath = '../../dataset/Data Integration/data/'
    Facility.to_csv(exportPath+'Facility.csv', index=False)
    Price.to_csv(exportPath+'Price.csv', index=False)
    Contact.to_csv(exportPath+'Contact.csv', index=False)
    Address.to_csv(exportPath+'Address.csv', index=False)
    Location.to_csv(exportPath+'Location.csv', index=False)
    Calendar.to_csv(exportPath+'Calendar.csv', index=False)
    CalendarDates.to_csv(exportPath+'CalendarDates.csv', index=False)
    print('export done.')
    #%%
