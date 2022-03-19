import requests
import json

api_address = "http://api.openweathermap.org/data/2.5/weather?appid=6193c6489e570568ec4daa153cc0976c&q="
while True:
    address = input('Enter location: ')
    if len(address) < 1: break


    url = api_address + address
    details = requests.get(url).json()


    print(json.dumps(details, indent=4))

    data = details["weather"][0]["description"]
    print(data)
