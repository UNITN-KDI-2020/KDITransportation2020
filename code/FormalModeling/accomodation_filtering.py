'''
This file parse the accomodation dataset and filter
the needed information based on the schema.

@carbogninalberto
'''
import pandas as pd
import json

if __name__ == "__main__":
    pd.options.mode.chained_assignment = None
    print("1. Loading CSV file into a pandas dataframe")
    # loading the elaborated dataset from previous phase
    dataset_path = '../../dataset/Scope Definition & Inception/data/accomodation/Provincia-Autonoma-di-Trento---Elenco-strutture-extra-alberghiere_elaborated.csv'
    dataset = pd.read_csv(dataset_path, sep=",", encoding="ISO-8859-1", error_bad_lines=False, warn_bad_lines=False)

    # extracting
    accomodation_typologies = dataset['Tipologia'].unique()
    print(accomodation_typologies)

    filtered_dataset = dataset[['Tipologia', 'Telefono', 'Indirizzo posta elettronica', 'Sito internet', 'Prezzo', 'Comune', 'Provincia', 'Indirizzo', 'CAP localita', 'Altitudine localita turistica']]
    filtered_dataset.rename(columns={
        'Tipologia': 'Type',
        'Telefono': 'Phone',
        'Sito internet': 'Website',
        'Prezzo': 'Price',
        'Comune': 'City',
        'Provincia': 'Province',
        'Indirizzo': 'Street', # to be extracted the number
        'CAP localita': 'CAP',
        'Indirizzo posta elettronica': 'Email',
        'Altitudine localita turistica': 'Altitude'
        }, inplace=True)
    filtered_dataset.to_json('../../dataset/Formal Modeling/data/accomodations.json', orient='records', lines=False)
    #print(out)
    #'../../dataset/Formal Modeling/data/accomodations.json',
    #print(out[0])
    #with open('../../dataset/Formal Modeling/data/accomodations.json', 'w') as f:
    #    json.dump(out, f, ensure_ascii=False, indent=4)

    