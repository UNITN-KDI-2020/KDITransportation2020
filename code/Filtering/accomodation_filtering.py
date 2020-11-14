'''
This file parse the accomodation dataset and filter
the needed information based on the schema.

@carbogninalberto
'''
import pandas as pd

if __name__ == "__main__":
    print("1. Loading CSV file into a pandas dataframe")
    # loading the elaborated dataset from previous phase
    dataset_path = '../../dataset/Scope Definition & Inception/data/accomodation/Provincia-Autonoma-di-Trento---Elenco-strutture-extra-alberghiere_elaborated.csv'
    dataset = pd.read_csv(dataset_path, sep=",", encoding="ISO-8859-1", error_bad_lines=False, warn_bad_lines=False)

    # extracting
    accomodation_typologies = dataset['Tipologia'].unique()
    print(accomodation_typologies)

    filtered_dataset = dataset[['Tipologia', 'Prezzo', 'Comune', 'Frazione', 'Provincia', 'Indirizzo', 'CAP localita', 'Altitudine localita turistica']]
    filtered_dataset.rename(columns={'Altitudine localita turistica': 'Altitude'}, inplace=True)
    filtered_dataset.to_json('../../dataset/Informal Modeling/data/accomodations.json', orient='records', lines=True)

    