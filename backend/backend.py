import requests
from dotenv import load_dotenv
import os

load_dotenv()

def getrainfall(lat=37.8267, long=-122.4233):
    url = f"https://api.darksky.net/forecast/{os.environ.get('weatherKey')}/{str(lat)},{str(long)}"
    r = requests.get(url).json(indent=4)
    print(r['daily'])
    print()
    return r
