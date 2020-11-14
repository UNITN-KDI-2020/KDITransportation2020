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
    ds_path = '../../dataset/Formal Modeling/data/parking_areas.json'

    with open(ds_path, 'r') as ds_file:
        dataset = json.load(ds_file)
        # iterating each row
        for row in dataset:            
            # creating location
            location = Location(float(row['Latitude']), float(row['Longitude']), None)
            # generate address
            address = Address(
                province=None,
                city=row['City'],
                street=None,
                number=None,
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
                type="PARKINGAREA - {}".format(row['Name'] if row['Name'] != None else ''),
                price=price,
                contact=contact,
                ranking=1,
                address=address,
                calendar=None
            )
            data.append(facility.toJSON())
    #print(data)
    print("2. Exporting assured json data")       
    ds_out_path = '../../dataset/Formal Modeling/data/parking_areas_assured.json'
    with open(ds_out_path, 'w') as ds_out_file:
        json.dump(data, ds_out_file)