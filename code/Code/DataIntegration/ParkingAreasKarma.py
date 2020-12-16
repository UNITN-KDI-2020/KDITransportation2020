# -*- coding: utf-8 -*-
"""

@author: Carbognin Alberto
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import json
import random

enumDict = {'FuelStation':0,
                'ParkingArea':1,
                'RailwayStation':2,
                'BusStation':3,
                'CarSharingPark':4,
                'BikeSharingPark':5,
                'Campsite':6}

if __name__ == "__main__":
    print("Loading dataSet...")

    print('Start making datasets...')
    Facility = pd.DataFrame(columns=['FacilityID','RouteID','Price','Contact','FacilityEnum','Address','Calendar'])
    Price =pd.DataFrame(columns=['FacilityID','TicketID','AutonomousTransportID','Cost','CurrencyType'])
    Contact = pd.DataFrame(columns=['AgencyID','FacilityID','Phone','Email','Website'])
    Address = pd.DataFrame(columns=['FacilityID','RouteID','Province','City','Street','Number','Cap','Location'])
    Location = pd.DataFrame(columns=['AddressID','StopId','Latitude','Longitude','Altitude'])
    Calendar = pd.DataFrame(columns=['FacilityID','StopTimesID','ServiceID','Monday','Tuesday','Wednesday',
                                     'Thursday','Friday','Saturday','Sunday','StartDate','EndDate','Exceptions'])
    CalendarDates = pd.DataFrame(columns=['CalendarId','ServiceId','Date','ExceptionType'])


    #Load the file

    json_file_path = '../../dataset/Formal Modeling/data/parking_areas_assured.json'

    with open(json_file_path, 'r') as j:
        parking_areas = json.loads(j.read())
        #fuel_pumps = json.loads('../../dataset/Formal Modeling/data/fuel_pumps_assured.json')

        print(json.loads(parking_areas[0]))

        print("Found: {} records in the dataset.".format(len(parking_areas)))
        
        for i in range(len(parking_areas)):
            parking_area = parking_areas[i]
            
            if i%300 == 0:
                print("Processing {}/{} record.".format(i, len(parking_areas)))            
            record = json.loads(parking_area)

            address = record['address']
            #print("\taddress:", address)

            location = address['location']
            contact = record['contact']

            # ['AgencyID','FacilityID','Phone','Email','Website']
            Contact.loc[i] = [None, i, contact['phone'], contact['email'], contact['website']]

            # ['AddressID','StopId','Latitude','Longitude','Altitude']
            Location.loc[i] = [i, None, location['latitude'], location['longitude'], location['altitude']]

            # ['FacilityID','RouteID','Province','City','Street','Number','Cap','Location']
            Address.loc[i] = [None, None, address['province'], address['city'], address['street'], address['number'], address['cap'], i]

            # ['FacilityID','RouteID','Price','Contact','FacilityEnum','Address','Calendar']
            Facility.loc[i] = [i, None, None, i, 1, i, None]





        
        print('Start exporting datasets...')
        exportPath = '../../dataset/Data Integration/data/ParkingAreas/'
        os.mkdir(exportPath)
        Facility.to_csv(exportPath+'Facility.csv')
        Price.to_csv(exportPath+'Price.csv')
        Contact.to_csv(exportPath+'Contact.csv')
        Address.to_csv(exportPath+'Address.csv')
        Location.to_csv(exportPath+'Location.csv')
        Calendar.to_csv(exportPath+'Calendar.csv')
        CalendarDates.to_csv(exportPath+'CalendarDates.csv')
        print('export done.')
        
