
import requests
import datetime

USERNAME = "hasib104"
TOKEN = "fdsfdsfds4fsd2f1sf4sdf"
GRPAH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

response = requests.post(url=pixela_endpoint, json=parameters)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : "graph1",
    "name" : "Running Graph",
    "Unit" : "Km",
    "type" : "float",
    "color" : "ajisai",
}

headers = {
    "X-USER-TOKEN" : TOKEN,
}

graph_response = requests.post(url=graph_endpoint, json=graph_config, headers= headers)
#print(graph_response.text)

post_a_pixel_endpoint = f"{graph_endpoint}/{GRPAH_ID}"

#Using strftime()
today = datetime.datetime.now()
today_formatted = today.strftime("%Y%m%d")
#print(today_formatted)

post_a_pixel_config = {
    "date" : today_formatted,
    "quantity" : input("How many Kilometers did u run today? "),
}

post_a_pixel_response = requests.post(url=post_a_pixel_endpoint, json= post_a_pixel_config, headers=headers)
print(post_a_pixel_response.text)

put_a_pixel_config = {
    "quantity" : "2.00",
}
put_a_pixel_endpoint = f"{post_a_pixel_endpoint}/{today_formatted}"

# put_a_pixel_response = requests.put(url=put_a_pixel_endpoint, json=put_a_pixel_config, headers=headers)
# print(put_a_pixel_response.text)
#
# delete_a_pixel_response = requests.delete(url=put_a_pixel_endpoint, headers=headers)
# print(delete_a_pixel_response.text)
