'''
#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint

# Put the details of the dataset we're going to create into a dict.
dataset_dict = {
    'name': 'my_dataset_name',
    'notes': 'A long description of my dataset',
    'owner_org': 'org_id_or_name'
}

# Use the json module to dump the dictionary to a string for posting.
data_string = urllib.quote(json.dumps(dataset_dict))

# We'll use the package_create function to create a new dataset.
request = urllib2.Request(
    'http://167.99.139.12/api/action/package_create')

# Creating a dataset requires an authorization header.
# Replace *** with your API key, from your user account on the CKAN site
# that you're creating the dataset on.
request.add_header('Authorization', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJROWl1VnBwOVVhcGZSSkotS1hGQmRSSGJ5MFBxeFdUbUFsZm1WLWgxRG5KMmZ6STdoSS1OOHdNa3RCXy1OVS05SU95dF95NzBVemcxRmxsTSIsImlhdCI6MTYwNDE0NDM3MX0.G5fagLdlM3_qktnTTD82aiia_cEAZMCIT7VFuSlT1wY')

# Make the HTTP request.
response = urllib2.urlopen(request, data_string)
assert response.code == 200

# Use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(response.read())
assert response_dict['success'] is True

# package_create returns the created package as its result.
created_package = response_dict['result']
pprint.pprint(created_package)

'''