creds = {
    'email' : 'aparna.pal.1994@gmail.com',
    'password' : 'Ferrar1_',
    'subdomain': 'https://z3nplatformdevap.zendesk.com'
}

# Import the Zenpy Class
from zenpy import Zenpy

# Default
zenpy_client = Zenpy(**creds)
print("got here!")
print(zenpy_client)

zenpy_client.search(type='ticket')
