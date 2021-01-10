"""Simple function"""
# def greet():
#     print("Hello")
#     print("How are you?")
#     print("What are you upto nowadays?")
#
# greet()

"""#Function with variable"""
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How are you {name}?")
#
# greet_with_name("Hasib")

"""#function with more than one input"""
# def greet_with(name, location):
#     print(f"Hello! {name}")
#     print(f"Where are u from? {location}")
#
# greet_with("Hasib", "Bangladesh")

"""#function with keyword argument"""
# def greet_with(name, location):
#     print(f"Hello! {name}")
#     print(f"Where are u from? {location}")
#
# greet_with(name="Hasib", location="Bangladesh")
# greet_with(location="Bangladesh", name="Hasib")

import math
"""#Area Calculator"""
# coverage= 5
# def area_calculator(height, width):
#     area= height*width
#     paint_cans_needed= round(area/coverage)
#     # paint_cans_needed = math.ceil(area / coverage) #math.ceil fn
#     print(f"You need {paint_cans_needed} paint cans")
#
# h=int(input("Enter Height: "))
# w=int(input("Enter Width: "))
# area_calculator(height=h, width=w)

"""#Prime Number Checker"""
def prime_number_checker(n):
    if n==1:
        print("It's not a prime number")
    elif n%1 == 0 and n%n == 0:
        for counter in range(2, 4):
            if n%counter == 0:
                print()

        print("It's not a prime number")

    else:
        print("It's a prime number")

number= int(input("Enter a number: "))
print(number)
prime_number_checker(number)
