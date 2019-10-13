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
    def addrlatlng(self, addr):
        if '*' in addr:
            addr = addr.replace('*', '%20')
        addr = addr.replace(' ', '%20')  # delim --> `space`
        print(os.environ.get('mapboxKey'))
        url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{addr}.json?access_token={os.environ.get('mapboxKey')}"
        r = requests.get(url).json()
        print()
        print(r)
        print()
        r = r['features'][0]['center']
        return r[::-1]


    # to get rainfall over days for lat,lng
    def checkrainfall(self, addr):
        lat, lng = self.addrlatlng(addr)
        url = f"https://api.darksky.net/forecast/{os.environ.get('weatherKey')}/{lat},{lng}"
        r = requests.get(url)
        daily = r.json()['daily']['data']
        vals = list(map(lambda x: x['precipIntensityMax']*24, daily))
        return list(map(lambda x: round(x, 3), np.cumsum(vals)))

    # get elevation of given lat/lng
    def getelev(self, lat, lng):
        url = f"https://api.jawg.io/elevations?locations={lat},{lng}&access-token={os.environ.get('jawgKey')}"
        time.sleep(1)
        r = requests.get(url).json()
        return r[0]['elevation']

    # compare your elev to elev of surrounding areas
    def relativedanger(self, addr, r=0.03, n=10):
        center = self.addrlatlng(addr)
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

if __name__ == '__main__':
    l = logic()
    l.addrlatlng('319 trenton way menlo park ca 94025')
