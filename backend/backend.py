import requests
from dotenv import load_dotenv
import os

load_dotenv()
darksky = os.environ.get('darkskydarksky')

def rainfall(lat=42.3601, long=-71.0589):
    url = 'https://api.darksky.net/forecast/d64c249e442fb61d8a38236627633a13/37.8267,-122.4233'
    r = requests.get(url).json()
    print(r)
    print(darksky)
    return r
