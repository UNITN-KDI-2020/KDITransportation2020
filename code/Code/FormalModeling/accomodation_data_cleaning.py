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
    ds_path = '../../dataset/Formal Modeling/data/accomodations.json'

    with open(ds_path, 'r') as ds_file:
        dataset = json.load(ds_file)
        # iterating each row
        for row in dataset:            
            # creating location
            location = Location(None, None, float(row['Altitude']))
            # cleaning address and extracting number
            cleaned_street = row['Street'].replace('\/', '/')
            numbers = re.findall("[0-9]{1,4}/?[A-Za-z]?", cleaned_street)
            if len(numbers) > 0:
                street_number = numbers[0]
            else:
                street_number = ""
            # cleaned address
            cleaned_street = cleaned_street.split(',')[0].split('-')[0]
            # generate address
            address = Address(
                province=row['Province'],
                city=row['City'],
                street=cleaned_street,
                number=str(street_number),
                cap=int(row['CAP']),
                location=location
            )
            # generate price
            price = Price(row['Price'])
            # generate contact
            contact = Contact(
                phone=row['Phone'],
                email=row['Email'],
                website=row['Website']
            )
            #generate facility
            facility = Facility(
                type=row['Type'],
                price=price,
                contact=contact,
                ranking=1,
                address=address,
                calendar=None
            )
            data.append(facility.toJSON())
    #print(data)
    print("2. Exporting assured json data")       
    ds_out_path = '../../dataset/Formal Modeling/data/accomodations_assured.json'
    with open(ds_out_path, 'w') as ds_out_file:
        json.dump(data, ds_out_file)