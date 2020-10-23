'''
This file parse the accomodation dataset and fill
the missing data based on the available information.

We assumed that the prices fit a gaussian distribution.

@carbogninalberto
'''
import pandas as pd
import numpy as np
import math
import random
import scipy.stats as st

def computeMean(x):
    sum_x = 0
    n = len(x)
    for i in range(0,n):
        sum_x += float(x[i])
    mean = sum_x / n
    return mean

def computeStdDev(x):
    mean = computeMean(x)
    sum_squares = 0
    n = len(x)
    for i in range(0,n):
        sum_squares += pow((x[i] - mean), 2)
    std_dev = math.sqrt(sum_squares / (n - 1))
    return std_dev

if __name__ == "__main__":
    print("1. Loading CSV file into a pandas dataframe")
    dataset_path = '../dataset/Scope Definition & Inception/data/accomodation/Provincia-Autonoma-di-Trento---Elenco-strutture-extra-alberghiere.csv'
    dataset = pd.read_csv(dataset_path, sep=";", encoding="ISO-8859-1", error_bad_lines=False, warn_bad_lines=False)
    
    # extracting the campsites
    # campsites1 = dataset.loc[dataset['Tipologia']=="CAMPEGGIO"]
    # campsites2 = dataset.loc[dataset['Tipologia']=="CAMPEGGIO PARCO PER VACANZE"]
    # frames = [campsites1, campsites2]
    # campsites = pd.concat(frames)
    # print("\t- campsites dataframe:\n{}".format(campsites))
    # print("\t- prices:\n{}".format(campsites['Prezzo']))

    # extracting the affittacamere
    extracted_typology = dataset.loc[dataset['Tipologia']=="AFFITTACAMERE"]
    print("\t- dataframe:\n{}".format(extracted_typology))
    
    prices = extracted_typology['Prezzo'].tolist()
    print("\t- prices:\n{}".format(extracted_typology['Prezzo']))
    mean = computeMean(prices)
    std = computeStdDev(prices)
    print('\t- Mean: {} Std: {}'.format(mean, std))

    for i in range(len(extracted_typology)):
        if float(extracted_typology.iloc[i]['Prezzo']) == 0.0:
            random_price = abs(np.random.normal(mean, std, 1)[0])
            print(random_price)
            extracted_typology.iloc[i]['Prezzo'] = random_price
    
    not_extracted_typology = dataset.loc[dataset['Tipologia']!="AFFITTACAMERE"]

    final_dataset = pd.concat([not_extracted_typology, extracted_typology])
    dataset_path = '../dataset/Scope Definition & Inception/data/accomodation/Provincia-Autonoma-di-Trento---Elenco-strutture-extra-alberghiere_elaborated.csv'
    final_dataset.to_csv(dataset_path)    

    