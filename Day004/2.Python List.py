"""#Basic Python List"""
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey" "Georgia", "Connecticut"]
# print(states_of_america[0]) #positive index
# print(states_of_america[1])
# print(states_of_america[-1]) #negative index

"""#Editing &Adding to the list"""

# states_of_america[1] = "Pencilvanya"
# print(states_of_america)
# states_of_america.append("Hasibland") #append adds one item
# print(states_of_america)
# states_of_america.extend(["Kamalland", "Arafland"]) #extend adds multiple items
# print(states_of_america)

"""#Who is paying the bill using Split function"""
import random
# test_seed=int(input("Give a seed number: "))
# random.seed(test_seed)
# everyones_name= input("Enter everybody's name separated by a comma and space (, ) \n")
# everyones_name_split= everyones_name.split(", ")
# print(everyones_name_split)
#
# no_of_people = len(everyones_name_split)
# print(f"Number of peoople enjoying the meal: {no_of_people}")
# bill_payer_no= random.randint(0, no_of_people - 1) #As the countng starts from 0 we subtract 1 from no_of_people.
# bill_payer_name = everyones_name_split[bill_payer_no]
#
# print(f"The person paying the bill for everyone's food is {bill_payer_name}")

#all this could have been done by choice function

# test_seed=int(input("Give a seed number: "))
# random.seed(test_seed)
# everyones_name= input("Enter everybody's name separated by a comma and space (, ) \n")
# everyones_name_split= everyones_name.split(", ")
# print(everyones_name_split)
# bill_payer_name = random.choice(everyones_name_split)
# print(f"The person paying the bill for everyone's food is {bill_payer_name}")


"""#Getting rid of list index out of range error"""
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"]
# print(states_of_america)
# no_of_item_in_list = len(states_of_america)
# print(states_of_america[no_of_item_in_list -1]) #subtracting 1

"""#Treasure Spot"""
# row1 = ["a","b","c"]
# row2 = ["d","e","f"]
# row3 = ["g","h","i"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? \n")
#
# column = int(position[0])
# row = int(position[1])
#
# selected_row= (map[row- 1])
# selected_row[column-1]="X"
# print(f"{row1}\n{row2}\n{row3} \n")
# #or
# map[row-1][column-1]="X"
# print(f"{row1}\n{row2}\n{row3}")

"""#Rock, Paper & Scissor"""
print("Welcome to Rock, Paper & Scissor Game")
test_seed=input("Enter a seed number: ")
random.seed(test_seed)

person_choice=int(input("What do you choose? \nType 0 for Rock\nType 1 for Paper\nType 2 for Scissors.\n"))
if person_choice == 0:
    print("You Chose Rock")
elif person_choice == 1:
    print("You Chose paper")
else:
    print("You Chose Scissors")

computer_choice= random.randint(0, 2)
if computer_choice == 0:
    print("Computer randomed Rock")
elif computer_choice == 1:
    print("Computer randomed paper")
else:
    print("Computer randomed Scissors")

if person_choice == 0 and computer_choice == 0:
    print("Draw")
elif person_choice == 1 and computer_choice == 1:
    print("Draw")
elif person_choice == 2 and computer_choice == 2:
    print("Draw")
elif person_choice == 0 and computer_choice == 1:
    print("Computer Won")
elif person_choice == 0 and computer_choice == 2:
    print("You Won")
elif person_choice == 1 and computer_choice == 0:
    print("You Won")
elif person_choice == 1 and computer_choice == 2:
    print("Computer Won")
elif person_choice == 2 and computer_choice == 0:
    print("Computer Won")
else:
    print("Computer Won")
