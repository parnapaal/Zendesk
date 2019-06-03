from bs4 import BeautifulSoup
import requests
import json

# Set the request parameters
url = 'https://z3nplatformdevap.zendesk.com/api/v2/custom_roles.json'
user = 'aparna.pal.1994@gmail.com'
pwd = 'Ferrar1_'

# Do the HTTP get request
response = requests.get(url, auth=(user, pwd))


# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()

soup = BeautifulSoup(data, features="lxml")

newDictionary=json.loads(str(soup))
