import requests
import json
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

SID = os.getenv("SID")
TOKEN = os.getenv("TOKEN")

API_KEY = os.getenv("API_KEY")
LOC = os.getenv("LOC")

client = Client(SID, TOKEN)

url = os.getenv("LINK")
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
print("RealTime Fetched")

data = json.loads(response.text)
temperature = data["data"]["values"]["temperature"]
weatherCode = str(data["data"]["values"]["weatherCode"])
print("Data Fetched")

file = open("weather code.json",'r')
weatherCodes = json.load(file)
for keys in weatherCodes:
    for key in weatherCodes[keys]:
        if key == weatherCode:
            messageWeathercode = weatherCodes[keys][key]

print("Weather condition fetched")

message = f"\nHey Shaurya!\nThe current temperature is\nTemp:{temperature}_C\nWeather code: {weatherCode} ({messageWeathercode})."
message = client.messages.create(
    body=message,
    from_=os.getenv("FROM"),
    to=os.getenv("TO"),
)

print("Message Sent")