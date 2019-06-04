import requests
import json

# Set the request parameters
url = 'https://z3nplatformdevap.zendesk.com/api/v2/tickets.json'
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
#print(data)

print(json.dumps(data, indent=2))

#parsed = json.loads(response)
#print(json.dumps(parsed, indent=4, sort_keys=True))
    
# Example 1: Print the name of the first group in the list
#print( 'First group = ', data['groups'][0]['name'] )

#Example 2: Print the names of each organization
group_list = data['tickets']
for group in group_list:
    print(group['subject'])