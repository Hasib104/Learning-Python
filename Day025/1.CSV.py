
"""Basic data read + listing"""
# with open("weather_data.csv") as data:
#     contents = data.readlines()
#     print(contents)

# import csv
"""#Looping to see the values using csv.reader"""
# with open("weather_data.csv") as data:
#     contents = csv.reader(data)
#     temperature = []
#     for counter in contents:
#         print(counter)

"""#Extracting the temperatures without the label"""
# with open("weather_data.csv") as data:
#     contents = csv.reader(data)
#     temperature = []
#     for counter in contents:
#         if counter[1] != "temp": #skips the column title temp
#             temperature.append(int(counter[1]))
#
#     print(temperature)


import pandas
"""#Reading the csv using pandas"""
# data = pandas.read_csv("weather_data.csv")
# print(data)

"""#Extracting the temp from csv"""
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

"""#Converting from data frame"""

# data_dict = data.to_dict()
# print(data_dict)
#
# data_temp = data["temp"].to_list()
# print(data_temp)

"""#Avg temp of csv"""

data = pandas.read_csv("weather_data.csv")
# temp = data["temp"]
# data_temp = temp.to_list()
# total = 0
# for counter in data_temp:
#     total += counter
#
# print(total)
# avg = total/ len(data_temp)
# print(avg)

#or

# avg = sum(data_temp)/len(data_temp)
# print(avg)

#or using method
# print(data["temp"].mean())
#
# """#max value"""
# print(data["temp"].max())
#
# """#Get data in columns"""
# print(data["condition"])
# #or
# print(data.condition)

#get data from rows
# print(data[data.day == "Monday"])
# #printing the highest temp day
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.condition)

# monday = data[data.day == "Monday"]
# monday_temp_F = monday.temp * 9/5 +32
# print(monday_temp_F)

"""#Create a dataframe from scratch"""
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 59, 68]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")