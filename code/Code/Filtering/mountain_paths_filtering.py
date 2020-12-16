'''
This file parse the mountain paths dataset and filter
the needed information based on the schema.

@carbogninalberto
'''
import pandas as pd

if __name__ == "__main__":
    print("1. Loading CSV file into a pandas dataframe...")
    # loading the elaborated dataset from previous phase
    dataset_path = '../../dataset/Scope Definition & Inception/data/mountain_paths/Provincia-di-Trento---Sentieri.csv'
    dataset = pd.read_csv(dataset_path, sep=";", encoding="ISO-8859-1", error_bad_lines=False, warn_bad_lines=False)

    # filtering
    print("2. Filtering...")
    filtered_dataset = dataset[['Numero sentiero tratta', 'Competenza', 'Denominazione', 'Difficoltà', 'Località inizio', 'Località fine']]
    # filtered_dataset.rename(columns={'Longitudine': 'Longitude', 'Latitudine': 'Latitude'}, inplace=True)
    filtered_dataset.to_json('../../dataset/Informal Modeling/data/mountain_paths.json', orient='records', lines=True)
    print("3. Exported!")
