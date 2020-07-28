import requests
import json
from pprint import pprint

url = "https://api.fitbit.com/1/user/-/profile.json"
headers = {"Authorization":  "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMkJOSE4iLCJzdWIiOiI4NlI5NVIiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJhY3QgcnNldCBybG9jIHJ3ZWkgcmhyIHJudXQgcnBybyByc2xlIiwiZXhwIjoxNTk0NTUwNjIxLCJpYXQiOjE1OTM5NDYwNDd9.i3eWBaNmbFXbr1TOcqVVrav70zZB2B3z7ViL9uNrqhM"}

data = requests.get(url,headers=headers).json()

pprint(data)

print("full_Name :",data["user"]["fullName"])
print("my_age :",data["user"]["age"])
print("average_Daily_Steps :",data["user"]['averageDailySteps'])

