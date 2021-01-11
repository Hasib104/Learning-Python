############DEBUGGING#####################

# Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()
#
# def my_function():
#   for i in range(1, 21): #should be 21 to reach i==20
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
#
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5) #should be 0-5 instead of 1-6
# print(dice_imgs[dice_num])

# Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
#
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994: #need to add =
#   print("You are a Gen Z.")

# Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# age = int(input("How old are you?")) #needs int
# if age > 18:
#     print(f"You can drive at age {age}.") #needs indentationand f-string

#Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# print(pages)
# word_per_page = int(input("Number of words per page: ")) #Should be = instead of ==
# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)
#
# mutate([1,2,3,5,8,13])

# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item) #needs indentation
#   print(b_list)
#
# mutate([1,2,3,5,8,13])

"""#Exercise"""
#Even or odd
# number = int(input("Which number do you want to check?"))
#
# if number % 2 = 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# number = int(input("Which number do you want to check?"))
#
# if number % 2 == 0: #Should be == instead of =
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

#Leap year
# year = input("Which year do you want to check?")
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

# year = int(input("Which year do you want to check?")) #year Should be int
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

#FizzBuzz
# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])

# for number in range(1, 101):
#   if number % 3 == 0 and number % 5 == 0: #Should be and instead of or
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number) #its an int not list