
import requests
from twilio.rest import Client
import os

api_key = "9bd6a590543da984180c8afd61272ed4"
account_sid = "AC8ed406ce4687e33b304a086a05b472f8"
auth_token = "0c4a9f8db145aced1341f64ca7221808"

parameters = {
    "lat" : 23.738205,
    "lon" : 90.407219,
    "appid": api_key,
    "exclude" : "current,minutely,daily",
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
#slicing to get 0-11
data_slice = data["hourly"][:12]

will_rain = False
for hour_data in data_slice:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an Umbrella.",
        from_='+19362336529',
        to='+8801558985075',
    )
    print(message.status)

#print(data_slice)
#print(data["hourly"][0]["weather"][0]["id"])