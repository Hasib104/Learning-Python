import random
"""#Basic Loop"""
# fruits= ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

"""#Avg Height Calculator"""

# student_height_list= input("Enter a list of height: ")
# student_height_list= student_height_list.split(",")
# print(student_height_list)
#
# for int_height in range(0, len(student_height_list)):
#     student_height_list[int_height]= int(student_height_list[int_height])
# print(student_height_list)
# total_heights=0
# total_students=0
#
# for height in student_height_list:
#     total_heights+= height
# print(total_heights)
#
# for student in student_height_list:
#     total_students+=1
# print(total_students)
#
# avg_height= round(total_heights/total_students)
# print(avg_height)

"""#Highest Score"""
# print("Welcome to Highest score Calculator.")
# scores= input("Enter the list of scores: ")
# scores_split= scores.split(",")
# for n in range(0, len(scores_split)):
#     scores_split[n]= int(scores_split[n])
# print(scores_split)
#
# high_score=0
# for score in scores_split:
#     if score>high_score:
#         high_score=score
# print(f"The highest score in the class is {high_score}")

"""#Range function"""
# for number in range(1,10): #It goes from 0-9(number<10)
#     print(number)
#
# for number in range(1,11): #Now It goes from 0-10(number<11)#Solution
#     print(number)


"""#Counting 1-100"""
# print("Welcome to range counter")
# starting_no=int(input("Starting point: "))
# ending_no=int(input("Ending point: "))
#
# total=0
# for starting_no in range(starting_no, ending_no+1):
#     total+= starting_no
# print(total)

"""Adding only Even Numbers"""

# starting_no=int(input("Starting point: "))
# print(starting_no)
# ending_no=int(input("Ending point: "))
# print(ending_no)
#
#
# total=0
# for starting_no in range(starting_no, ending_no+1):
#     if starting_no % 2 == 0:
#         total += starting_no
# print(f"Total:{total}")

"""#FizzBuzz"""
# starting_no=int(input("Starting point: "))
# print(starting_no)
# ending_no=int(input("Ending point: "))
# print(ending_no)
#
# for starting_no in range(1, ending_no+1):
#     if starting_no % 3 == 0 and starting_no % 5 == 0:
#         print("FizzBuzz")
#     elif starting_no % 3 == 0:
#         print("Fizz")
#     elif starting_no % 5 == 0:
#         print("Buzz")
#     else:
#         print(starting_no)

"""PyPassword Generator"""
print("Welcome to PyPassword Generator")
# test_seed= int(input("Enter a seed number: "))
# random.seed(test_seed)
# print(test_seed)
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
print(nr_letters)
nr_symbols = int(input(f"How many symbols would you like?\n"))
print(nr_symbols)
nr_numbers = int(input(f"How many numbers would you like?\n"))
print(nr_numbers)

#easy password generator using string
# r_letters= "" #it's a string
# for letter in range(0, nr_letters):
#     r_letters += random.choice(letters)
#
# print(r_letters)
#
# r_symbols="" #it's a string
# for symbol in range(0, nr_symbols):
#     r_symbols += random.choice(symbols)
#
# print(r_symbols)
#
# r_numbers="" #it's a string
# for number in range(0, nr_numbers):
#     r_numbers += random.choice(numbers)
# print(r_numbers)
#
#
# password= r_letters+r_symbols+r_numbers
# print(password)
#
# random.shuffle(password) #string does not support item assignment
# print(password)

#random password generator using shuffle

r_letters_list= []
for letter in range(0, nr_letters):
    r_letters_list += random.choice(letters)

#print(r_letters_list)

r_symbols_list= []
for symbol in range(0, nr_symbols):
    r_symbols_list += random.choice(symbols)

#print(r_symbols_list)

r_numbers_list =[]
for number in range(0, nr_numbers):
    r_numbers_list += random.choice(numbers)

#print(r_numbers_list)

#password generating in order

password_list = []
password_list = r_letters_list+r_symbols_list+r_numbers_list
print(f"Password generating in order: {password_list}")

#password generating randomly

random.shuffle(password_list)
print(f"Password generating randomly: {password_list}")
print(type(password_list))

password_str = ""

for string in password_list:
    password_str += string
    print(password_str)

print(f"Your password is: {password_str}")
print(type(password_str))