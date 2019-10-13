import requests
from dotenv import load_dotenv
import os

load_dotenv()

def rainfall(lat=37.8267, long=-122.4233):
    url = f"https://api.darksky.net/forecast/{os.environ.get('weatherKey')}/{str(lat)},{str(long)}"
    r = requests.get(url).json()
    print(os.environ.get('weatherKey'))
    w = os.environ.get('weatherKey')
    print(w)
    return r
