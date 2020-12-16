'''
This file parse the parking areas dataset and filter
the needed information based on the schema.

@carbogninalberto
'''
import pandas as pd

if __name__ == "__main__":
    print("1. Loading CSV file into a pandas dataframe...")
    # loading the elaborated dataset from previous phase
    dataset_path = '../../dataset/Scope Definition & Inception/data/parking_areas/Mappa-dei-parcheggi-in-Italia.csv'
    dataset = pd.read_csv(dataset_path, sep=";", encoding="ISO-8859-1", error_bad_lines=False, warn_bad_lines=False)

    # filtering
    print("2. Filtering...")
    filtered_dataset = dataset[['Longitudine', 'Latitudine', 'Comune', 'Provincia', 'Regione', 'Nome']]
    # filtered_dataset.rename(columns={'Longitudine': 'Longitude', 'Latitudine': 'Latitude'}, inplace=True)
    filtered_dataset.to_json('../../dataset/Informal Modeling/data/parking_areas.json', orient='records', lines=True)
    print("3. Exported!")
