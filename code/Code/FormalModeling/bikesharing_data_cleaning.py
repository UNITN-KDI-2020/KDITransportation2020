'''
Data need to be cleaned by unused spaces and exported in a
easy manner to be integrated

@carbogninalberto
'''
import pandas as pd
import json
import re
from models import Location, Address, Facility, Price, Contact

if __name__ == '__main__':
    pd.options.mode.chained_assignment = None

    data = []
    print("1. Importing json data")
    ds_path = '../../dataset/Informal Modeling/data/bikesharing.json'

    with open(ds_path, 'r') as ds_file:
        dataset = json.load(ds_file)
        # iterating each row
        for row in dataset:            
            # creating location
            location = Location(float(row['position'][1]), float(row['position'][0]), None)
            id_address = row['id'].split(' - ')

            numbers_1 = re.findall("[0-9]{1,4}/?[A-Za-z]?", row['id'])
            numbers_2 = re.findall("[0-9]{1,4}/?[A-Za-z]?", row['address'])
            print(numbers_1, numbers_2)
            if len(numbers_1) > 0 or len(numbers_2) > 0:
                if len(numbers_1) >= len(numbers_2):
                    street_number = numbers_1[0]
                else:
                    street_number = numbers_2[0]
            else:
                street_number = ''
            street = row['address'].split(' - ')[0].split(',')[0].replace(street_number, '')

            city = id_address[len(id_address)-1]
            print(street)
            print(street_number)
            print(city)
            print("------------------------")
            # generate address
            address = Address(
                province='Trento',
                city=city,
                street=street,
                number=street_number,
                cap=None,
                location=location
            )
            # generate price
            price = None
            # generate contact
            contact = Contact(
                phone=None,
                email=None,
                website=None
            )
            #generate facility
            facility = Facility(
                type="BIKESHARINGPARK - {}".format(row['name'] if row['name'] != None else ''),
                price=price,
                contact=contact,
                ranking=1,
                address=address,
                calendar=None
            )
            data.append(facility.toJSON())
    #print(data)
    print("2. Exporting assured json data")       
    ds_out_path = '../../dataset/Formal Modeling/data/bikesharing_assured.json'
    with open(ds_out_path, 'w') as ds_out_file:
        json.dump(data, ds_out_file)