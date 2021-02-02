
"""#ISS Position using requests"""
import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# #print(response)
# response.raise_for_status() #raises exception depending on the error
# data = response.json()
# print(data)
# data = response.json()["iss_position"]
# print(data)
# data = response.json()["iss_position"]["longitude"]
# print(data)
#
# lonitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
#
# iss_position = (lonitude, latitude)
# print(iss_position)

"""#Sunrise-Sunset with API Parameters"""
import datetime

MY_LAT = 23.738782
MY_LNG = 90.409534

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LNG,
    "formatted" : 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
#print(data)

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
# print(sunrise.split("T"))
# print(sunrise.split("T")[1])
# print(sunrise.split("T")[1].split(":"))
# print(sunrise.split("T")[1].split(":")[0])
print(sunset)

time_now = datetime.datetime.now()
#print(time_now)