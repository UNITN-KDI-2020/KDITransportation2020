# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 18:34:31 2020

@author: Omid Jadidi
"""


#%%
import numpy as np
import pandas as pd
#%%

print(os.getcwd())
os.chdir(os.getcwd())
#%%
if __name__ == '__main__':
    
    enumDict = {'FuelStation':0,
                'ParkingArea':1,
                'RailwayStation':2,
                'BusStation':3,
                'CarSharingPark':4,
                'BikeSharingPark':5,
                'Campsite':6}
    # print(enumDict.keys())
    enumDataFram = pd.DataFrame(columns=(['FacilityEnum','ID']))
    enumDataFram['FacilityEnum'] = enumDict.keys()
    enumDataFram['ID'] = enumDict.values()
#%%
    ds_out_path = '../../dataset/Data Integration/data/FacilityEnum.csv'
    enumDataFram.to_csv(ds_out_path)
    print("FacilityEnum Created. ")