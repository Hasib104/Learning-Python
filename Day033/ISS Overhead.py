import requests
import datetime
import smtplib
import time

MY_EMAIL = "hasib104.python@gmail.com"
PASSWORD = "Pp123456"

MY_LAT = 23.738782
MY_LNG = 90.409534

def is_iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True

def is_night():

    parameters = {
        "lat" : MY_LAT,
        "lng" : MY_LNG,
        "formatted" : 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    #print(data)

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    # print(sunrise.split("T"))
    # print(sunrise.split("T")[1])
    # print(sunrise.split("T")[1].split(":"))
    # print(sunrise.split("T")[1].split(":")[0])
    print(sunset)

    #just need the hour,  .hour
    time_now = datetime.datetime.now().hour
    #print(time_now)

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look up!\n\nThe iss is above you in the sky."
            )
