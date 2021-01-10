"""#Rollercoaster Height Checker"""
# print("Welcome to the Rollercoaster")
# height= int(input("What is your height in cm: "))
# print(height)
# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, You are not tall enough.")

"""#Odd or Even"""
# print("Wlcome to Odd or Even Calculator")
# number=int(input("Enter a number: "))
# print(number)
# if number % 2 ==0:
#     print("It's an Even number.")
# else:
#     print("It's an Odd number.")

"""#Modulo"""
# print(6 % 3) #remainder 0
# print(7%3) #remainder 1

"""#Nested Condition"""
# print("Welcome to the Rollercoaster")
# height= int(input("What is your height in cm: "))
# print(height)
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age=int(input("What is your age? "))
#     print(age)
#     if age<12:
#         print("\nPlease pay $5")
#     elif age<=18:
#         print("\nPlease pay $7")
#     else:
#         print("\nPlease pay $12")
# else:
#     print("Sorry, You are not tall enough.")

"""#BMI Nested"""
# height = float(input("enter your height in m: "))
# print(height)
# weight = float(input("enter your weight in kg: "))
# print(weight)
# BMI=round(float(weight/height**2), 2)
# if BMI<18.5:
#     print(f"Your BMI is {BMI}, you are underweight.")
# elif BMI<25:
#     print(f"Your BMI is {BMI}, you have a normal weight.")
# elif BMI<30:
#     print(f"Your BMI is {BMI}, you are slightly overweight.")
# elif BMI<35:
#     print(f"Your BMI is {BMI}, you are obese.")
# else:
#     print(f"Your BMI is {BMI}, you are clinically obese.")

"""#Leap Year"""
#Nested Conditional Statement
# print("Welcome to Leap Year Calculator")
# year=int(input("Input a year: "))
# print(year)
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print(f"{year} is leap year")
#         else:
#             print(f"{year} is not leap")
#     else:
#         print(f"{year} is not leap")
# else:
#         print(f"{year} is not leap")

#Shortcut using and function
# print("Welcome to Leap Year Calculator")
# year=int(input("Input a year: "))
# print(year)
#
# if year%4 == 0 and year%100 == 0 and year%400 == 0 :
#     print(f"{year} is leap year")
# elif year%4 == 0 and year%100 != 0 and year%400 != 0 :
#     print(f"{year} is leap year")
# elif year%4 == 0 and year%100 == 0 and year%400 != 0 :
#     print(f"{year} is not leap year")
#
# else:
#     print(f"{year} is not leap")

"""#Rollercoaste with photo bill"""
# print("Welcome to the Rollercoaster")
# height= int(input("What is your height in cm: "))
# print(height)
# bill=0
#
# if height >= 120:
#      print("You can ride the rollercoaster!")
#      age=int(input("What is your age? "))
#      print(age)
#      if age<12:
#          bill=5
#          print("\nChild ticket is $5")
#      elif age<=18:
#          bill=7
#          print("\nYoungster ticket is $7")
#        elif age>=45 and age<=55:
#            print("Have a free ride on us")
#      else:
#          bill=12
#          print("\nAdults ticket is $12")
#      photo=input("Do you want photo taken? (Y/N) ")
#      print(photo)
#      if photo == "Y":
#         bill + 3
#
#      print(f"Total bill of your ride is ${bill}") #using indentation to print the bill with or without the photo with a single pring, no need to use else statement
#
# else:
#      print("Sorry, You are not tall enough.")

"""#Pizza Order"""
# print("Welcome to our pizzaria")
# size= input("What size of pizza do you want? (S, M, or L) ")
# print(size)
# pepperoni= input("Do want pepperoni in your pizza? (Y/N) ")
# print(pepperoni)
# cheese= input("Do you want Extra cheese in your pizza? (Y/N) ")
# print(cheese)
# bill=0
# if size == "S":
#     bill=15
#     print(f"Price for Small pizza is ${bill}")
#     if pepperoni == "Y":
#         bill= bill+2
#     if cheese == "Y":
#         bill= bill+1
#     print(f"Total cost for your Small pizza is ${bill}")
# elif size=="M":
#     bill = 20
#     print(f"Price for Medium pizza is ${bill}")
#     if pepperoni == "Y":
#         bill= bill+3
#     if cheese == "Y":
#         bill= bill+1
#     print(f"Total cost for your Medium pizza is ${bill}")
# elif size=="L":
#     bill = 25
#     print(f"Price for Large pizza is ${bill}")
#     if pepperoni == "Y":
#         bill= bill+3
#     if cheese == "Y":
#         bill= bill+1
#     print(f"Total cost for your Large pizza is ${bill}")
# else:
#     print("Wrong input.\nPlease start over.")

"""#Love Calculator"""
# print("Welcome to Love Calculator")
# name1=input("What is your name? ")
# name1= name1.lower()
# name2=input("What is your better half's name? ")
# name2=name2.lower()
#
# t_occurs=0
# r_occurs=0
# u_occurs=0
# e_occurs=0
# t_r_u_e_total=0
#
# l_occurs=0
# o_occurs=0
# v_occurs=0
# l_o_v_e_total=0
#
# print(f"TRUE For {name1} & {name2}")
# if name1.lower().count("t") >=0 or name2.lower().count("t") >= 0:
#     t_occurs+= name1.lower().count("t")+name2.lower().count("t")
#     print(f"T occurs {t_occurs} times")
#     if name1.lower().count("r") >= 0 or name2.lower().count("r") >= 0:
#         r_occurs += name1.lower().count("r")+name2.lower().count("r")
#         print(f"R occurs {r_occurs} times")
#         if name1.lower().count("u") >= 0 or name2.lower().count("u") >= 0:
#             u_occurs += name1.lower().count("u")+name2.lower().count("u")
#             print(f"U occurs {u_occurs} times")
#             if name1.lower().count("e") >= 0 or name2.lower().count("e") >= 0:
#                 e_occurs += name1.lower().count("e")+name2.lower().count("e")
#                 print(f"E occurs {e_occurs} times")
#                 t_r_u_e_total=t_occurs+r_occurs+u_occurs+e_occurs
#                 print(f"True Occurs {t_r_u_e_total} times")
# else:
#     print()
#
# print(f"LOVE For {name1} & {name2}")
# e_occurs=0
# if name1.lower().count("l") >=0 or name2.lower().count("l") >= 0:
#     l_occurs+= name1.lower().count("l")+name2.lower().count("l")
#     print(f"L occurs {l_occurs} times")
#     if name1.lower().count("o") >= 0 or name2.lower().count("o") >= 0:
#         o_occurs += name1.lower().count("o")+name2.lower().count("o")
#         print(f"O occurs {o_occurs} times")
#         if name1.lower().count("v") >= 0 or name2.lower().count("v") >= 0:
#             v_occurs += name1.lower().count("v")+name2.lower().count("v")
#             print(f"V occurs {v_occurs} times")
#             if name1.lower().count("e") >= 0 or name2.lower().count("e") >= 0:
#                 e_occurs += name1.lower().count("e")+name2.lower().count("e")
#                 print(f"E occurs {e_occurs} times")
#                 l_o_v_e_total=t_occurs+r_occurs+u_occurs+e_occurs
#                 print(f"LOVE Occurs {l_o_v_e_total} times")
# else:
#     print()
#
# love_score=str(t_r_u_e_total)+str(l_o_v_e_total)
# love_score=int(love_score)
#
#
# print(f"Love Score = {t_r_u_e_total}{l_o_v_e_total}")
#
# if love_score < 10 or love_score > 90:
#     print(f"Your Score is {love_score}, you go together like coke and mentos")
# elif love_score >=40 and love_score <=50:
#     print(f"Your Score is {love_score}, you are alright together")
# else:
#     print(f"Your Score is {love_score}")

"""#Treasure Island"""
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
first_decision=input('You are at a cross road. Where do you want to go? "left" or "right"\n')
print(f"You decided to go {first_decision}")
if first_decision == "left":
    second_decision=input('You have come to a lake. There is an island the middle of the lake. Do u want to wait for a "boat" or "swim" across without waiting?\n')
    print(f"You wished a {second_decision}")
    if second_decision == "boat":
        third_decision=input('You have arrived at a island unharmed. There is a house with 3 doors. One "red", one "yellow", one "blue". Which color do you choose?\n')
        print(third_decision)
        if third_decision == "red":
            print("You have entered the room of forgotten tresaures. You Won.")
        elif third_decision == "yellow":
            print("You have entered a room full of Hyenas. Game Over.")
        else:
            print("You have entered a room of soul eater. Game Over.")
    else:
        print("The lake was full of flesh eating Piranhas. Game Over.")
else:
    print("You have come to a dead end. There is no turning back. Game over")
print("Thank you for playing.")

