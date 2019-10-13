import requests
import numpy as np
import os
from dotenv import load_dotenv
import math
import time
load_dotenv()

class logic:
    ''' some logic factored out of our API '''

    def __init__(self):
        pass

    # translate address to latitude/longitude
    def addrlatlng(addr='319*trenton*way*menlo*park*ca*94025'):
        addr = addr.replace('*', '%20')  # delim --> space
        maboxKey = os.environ.get('mapboxKey')


    # to get rainfall over days for lat,lng
    def checkrainfall(self, key, lat, lng):
        url = f"https://api.darksky.net/forecast/{os.environ.get('weatherKey')}/43.0731,89.4012"
        r = requests.get(url)
        daily = r.json()['daily']['data']
        vals = list(map(lambda x: round(x['precipIntensityMax']*24, 3), daily))
        return list(np.cumsum(vals))

    # get elevation of given lat/lng
    def getelev(self, lat, lng):
        time.sleep(1)
        url = f"https://api.jawg.io/elevations?locations={lat},{lng}&access-token={os.environ.get('jawgKey')}"
        r = requests.get(url).json()
        return r[0]['elevation']

    # compare your elev to elev of surrounding areas
    def relativeheight(self, center, r=0.03, n=10):
        ''' describe a circle around our lat,lng. r=0.03 --> 2 mile radius '''
        master = self.getelev(center[0], center[1])
        hits = 0
        for x in range(0, n+1):
            lat, lng = (
                center[0]+(math.cos(2 * math.pi / n * x) * r),   # x
                center[1] + (math.sin(2 * math.pi / n * x) * r)  # y
            )
            elev = self.getelev(lat, lng)
            if master < elev:
                hits += 1
        return hits/n
