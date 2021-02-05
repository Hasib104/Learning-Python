
import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

APPLICATION_ID = "5ea1e848"
APPLICATION_KEY = "ac3a4859cc9e5d1bcbd8286a60b9cc7b"
NUTRIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/f276d7e71e27a3dc198082db2a5d96ed/myWorkouts/workouts"

GENDER = "male"
WEIGHT_KG = 85
HEIGHT_CM = 176.784
AGE = 24

headers = {
    "x-app-id" : APPLICATION_ID,
    "x-app-key" : APPLICATION_KEY,
}

exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=NUTRIONIX_ENDPOINT, json=parameters, headers=headers)
data = response.json()
print(data)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

###Sheety expects us to record our activity in a nested root. As the endpoint #sheet_endpoint = "https://api.sheety.co/.../workouts" is named workouts, we have to nest it in "workout".

for item in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date" : today_date,
            "time" : now_time,
            "exercise" : item["name"].title(),
            "duration" : item["duration_min"],
            "calories" : item["nf_calories"],
        }

    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=HTTPBasicAuth('hasib104', 'dsfsdafsdfafdsfasdfsdfsd'))#sheety userame & password
    print(sheet_response.text)