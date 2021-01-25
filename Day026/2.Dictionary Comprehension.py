
"""#Creating Dictionary from list using Dictionary Comprehension"""
#Structure
# new_dict = {new_key:new_value for item in list} #creating dict from list
# new_dict = {new_key:new_value for (key, value) in dictionary.items()}
# new_dict = {new_key:new_value for (key, value) in dictionary.items() if test}
# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = {student:random.randint(1,100) for student in names}
# print(students_scores)
# passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
# print(passed_students)

"""Exercise"""
#8.1
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {item:len(item) for item in sentence.split()}
# print(result)
# print(type(result))
#9.1
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {day:(temp_c * 9/5)+32 for (day, temp_c) in weather_c.items()}
# print(weather_f)

"""#Iterate over a Pandas Dataframe"""

student_dic = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}

#Looping through dictionary
# for (key, value) in student_dic.items():
#     print(key)
#     print(value)
#     print(key, value)

#Looping through a data frame
import pandas
student_data_frame = pandas.DataFrame(student_dic)
#print(student_data_frame)
#using this method is not effective in pandas
# for (key, value) in student_data_frame.items():
#     #print(key)
#     #print(value)
#     print(key, value)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #print(index)
    #print(row)
    #print(row.student)
    #print(row.score)
    if row.student == "Angela":
        print(row.score)