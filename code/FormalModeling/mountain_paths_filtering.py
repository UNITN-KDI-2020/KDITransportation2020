'''
This file parse the mountain paths dataset and filter
the needed information based on the schema.

@carbogninalberto
'''
import pandas as pd

if __name__ == "__main__":
    pd.options.mode.chained_assignment = None
    print("1. Loading CSV file into a pandas dataframe...")
    # loading the elaborated dataset from previous phase
    dataset_path = '../../dataset/Scope Definition & Inception/data/mountain_paths/Provincia-di-Trento---Sentieri.csv'
    dataset = pd.read_csv(dataset_path, sep=";", encoding="ISO-8859-1", error_bad_lines=False, warn_bad_lines=False)

    # filtering
    print("2. Filtering...")
    filtered_dataset = dataset[['Denominazione', 'Quota fine', 'Località inizio']]
    filtered_dataset.rename(columns={
        'Denominazione': 'Name',
        'Quota fine': 'Altitude',
        'Località inizio': 'City'
        }, inplace=True)
    filtered_dataset.to_json('../../dataset/Formal Modeling/data/mountain_paths.json', orient='records', lines=False)
    print("3. Exported!")
