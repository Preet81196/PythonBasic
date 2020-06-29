import requests
import json
from datetime import datetime

api_address = "http://api.openweathermap.org/data/2.5/weather?appid=6193c6489e570568ec4daa153cc0976c&q="
while True:
    address = input('Enter any city location: ')
    if len(address) < 1: break


    url = api_address + address
    details = requests.get(url).json()


    #print(json.dumps(details, indent=4))
    city = details["name"]
    longitude = details["coord"]["lon"]
    latitude = details["coord"]["lat"]
    weather = details["weather"][0]["main"]
    weather_description = details["weather"][0]["description"]
    wind_speed = details["wind"]["speed"]
    wind_direction = details["wind"]["deg"]
    Cloudiness = details["clouds"]["all"]
    country = details["sys"]["country"]


    sunrise = details["sys"]["sunrise"]
    d = "1593390395"
    d = int(d[:10])
    Sunrise = datetime.fromtimestamp(d).strftime('%Y-%m-%d %I:%M:%S %p')


    sunset = details["sys"]["sunset"]
    d1 = "1593439002"
    d1 = int(d1[:10])
    Sunset = datetime.fromtimestamp(d1).strftime('%Y-%m-%d %I:%M:%S %p')


    temp = details["main"]["temp"]
    temp_min = details["main"]["temp_min"]
    temp_max = details["main"]["temp_max"]
    Atmospheric_pressure = details["main"]["pressure"]
    humidity = details["main"]["humidity"]
    visibility = details["visibility"]



    print("country ---> :",country)
    print("city name ---> ",city)
    print("longitude ---> :", longitude)
    print("latitude ---> :", latitude)
    print("weather_description ---> :",weather_description)
    print("weather ---> :", weather)
    print("wind speed ---> :",str(wind_speed) + "km/h")
    print("wind direction ---> :", wind_direction)
    print("Cloudiness ---> :",str(Cloudiness) + "%")
    print("temperature ----> :",str(temp-273.15) + "C")
    print("temp min ----> :", str(temp_min - 273.15) + "C")
    print("temp max ----> :", str(temp_max - 273.15) + "C")
    print("Atmospheric pressure ---> :",str(Atmospheric_pressure) + "hPa")
    print("humidity ---> :",str(humidity) + "%")
    print("visibility ---> :",str(visibility) + "km")
    print("sunrise ---> :",Sunrise)
    print("sunset ---> :",Sunset)
