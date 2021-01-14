
"""#Basic Packages"""
# import turtle
# timmy = turtle.Turtle()

#or

# from turtle import Turtle
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color('green')
# timmy.left(45)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
#
# from turtle import Screen
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

"""#Installing Prettytable and implementing"""
from prettytable import PrettyTable

table = PrettyTable() #creating object(table) from PrettyTable() class

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"]) #creating a column(Pokemon Name) and adding values
table.add_column("Type", ["Electric", "Water", "Fire"]) #creating a column(Type) and adding values

table.align = "l" #aligning the table from center to left aligned

print(table)
