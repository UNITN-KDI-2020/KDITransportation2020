'''
This file parse the accomodation dataset and filter
the needed information based on the schema.

@carbogninalberto
'''
import os
import json

if __name__ == "__main__":
    datasets_path = '../../dataset/Informal Modeling/data/added/bikesharing'
    print("dataset path: ", datasets_path)
    print("1. Loading CSV files into a pandas dataframe...")

    filenames = os.listdir(datasets_path)
    print(filenames)

    output_dataset = []

    print("2. Filtering...")
    for filename in filenames:
        with open(os.path.join(datasets_path, filename), 'r') as f: # open in readonly mode
            data = json.load(f)
            for row in data:
                output_dataset.append(row)

    with open('../../dataset/Informal Modeling/data/bikesharing.json', 'w') as json_file:
        json.dump(output_dataset, json_file)
    print("3. Exported!")
