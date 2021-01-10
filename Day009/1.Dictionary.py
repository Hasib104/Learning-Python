
"""#Basic Dictionary"""
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#
# }
# print(programming_dictionary["Function"])

#Adding items in dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

#creating dictionary and also wiping dictionary the dictionary if it existed before
# empty_dictionary= {}

#edit a item in dictionary same as adding
# programming_dictionary["Bug"] = "It's a bug."
# print(programming_dictionary["Bug"])

#Looping through the dictionary
# for counter in programming_dictionary:
#     print(counter)
#     print(programming_dictionary[counter])


"""#Grading Program"""
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99,
#   "Draco": 74,
#   "Neville": 62,
# }
# student_grades={}
# for counter in student_scores:
#     if student_scores[counter] >= 91:
#         student_grades[counter] = "Outstanding"
#     elif student_scores[counter] >= 81 and student_scores[counter] <91:
#         student_grades[counter] = "Exceeds Expectation"
#     elif student_scores[counter] >= 71 and student_scores[counter] <81:
#         student_grades[counter] = "Acceptable"
#     elif student_scores[counter] <= 70:
#         student_grades[counter] = "Fail"
#
# print(student_grades)

"""#Nesting"""

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }
#
# """#Nesting a list in a dictionary"""
#
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon",],
#     "Germany": ["Berlin", "Hamburg", "Stutgart"],
# }
#
"""#Nesting a dictionary in a dictionary"""
#
# travel_log = {
#     "France": {"cities_visited":["Paris", "Lille", "Dijon",], "total_visits": 12},
#     "Germany": {"cities_visited":["Berlin", "Hamburg", "Stutgart"], "total_visits": 12},
# }
#
# """#Nesting a dictionary in a list"""
#
# travel_log = [
#     {"country": "France",
#      "cities_visited":["Paris", "Lille", "Dijon",],
#      "total_visits": 12
#      },
#     {"country": "Germany",
#      "cities_visited":["Berlin", "Hamburg", "Stutgart"],
#      "total_visits": 12
#      },
# ]

"""Exercise"""

travel_log = [
    {"country": "France",
     "cities_visited":["Paris", "Lille", "Dijon",],
     "total_visits": 12
     },
    {"country": "Germany",
     "cities_visited":["Berlin", "Hamburg", "Stutgart"],
     "total_visits": 12
     },
]
print(len(travel_log))

def add_new_country(country_name, cities_visited, times_visited):
    new_country = {}
    new_country["country"] = country_name
    new_country["cities_visited"] = cities_visited
    new_country["total_visits"] = times_visited
    travel_log.append(new_country)

add_new_country("Russia", ["Moscow", "Saint Petersburg"], 2)
print(travel_log)


