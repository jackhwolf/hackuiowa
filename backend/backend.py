import requests
from dotenv import load_dotenv
import os

def rainfall(lat=42.3601, long=-71.0589):
    load_dotenv()
    darksky = os.environ.get('darkskydarksky')
    url = 'https://api.darksky.net/forecast/d64c249e442fb61d8a38236627633a13/37.8267,-122.4233'
    r = requests.get(url).json()
    print(darksky)
    return r
