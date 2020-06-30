import requests
import json
import pprint

from pprint import pprint

api_address = "http://api.currencylayer.com/live?access_key=107ba2de6963a4c5442a7ea6f651c305"

    #address = input('Enter any city location: ')
    #if len(address) < 1: break

url = api_address
details = requests.get(url).json()
pprint(details)

#work pending