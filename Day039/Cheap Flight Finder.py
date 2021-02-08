
from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/5199ee9856c4a4759620b3d82dfba8c6/flightDeals/prices"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "fc0HYYSZYLYhi3ZCFtGDY22DQjrU0hT1"

response = requests.get(url=SHEETY_PRICES_ENDPOINT)
data = response.json()["prices"]
pprint(data)

def update_destination_codes():
    for city in data:
        new_data = {
            "price" : {
                "iataCode" : city["iataCode"],
            }
        }
        response_1 = requests.put(
            url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
            json= new_data
        )
        print(response_1.text)

def get_destination_code(city_name):
    location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
    headers = {"apikey": TEQUILA_API_KEY}

    query = {"term": city_name,
             "location_types": "city"
             }

    response = requests.get(url=location_endpoint, headers=headers, params=query)
    results = response.json()["locations"]
    code = results[0]["code"]
    return code

if data[0]["iataCode"] == "":
    for row in data:
        row["iataCode"] = get_destination_code(row["city"])
    print(data)


    update_destination_codes()