# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 19:41:12 2020

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
    
    enumDict = {'Train':0,
                'Bus':1,
                'Car':2,
                'CableCar':3,
                'Bike':4,
                'Foot':5
                }
    # print(enumDict.keys())
    enumDataFram = pd.DataFrame(columns=(['TransportEnum','ID']))
    enumDataFram['TransportEnum'] = enumDict.keys()
    enumDataFram['ID'] = enumDict.values()
    #%%
    ds_out_path = '../../dataset/Data Integration/data/TransportEnum.csv'
    enumDataFram.to_csv(ds_out_path)
    print("TransportEnum Created. ")