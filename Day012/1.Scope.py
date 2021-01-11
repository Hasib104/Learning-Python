
"""#Scope"""

# enemies = 1
#
# def increase_enemies():
#     enemies = 2
#     print(f"Enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"Enemies outside function: {enemies}")

"""Local Scope"""

# def drink_potion():
#     potion_strength = 2 #Local Scope
#     print(potion_strength)
#
# drink_potion()
#print(potion_strength) #NameError: name 'potion_strength' is not defined

"""Global Scope"""

player_health = 10 #Global Scope

# def drink_potion():
#     potion_strength = 2
#     print(player_health)
#
# drink_potion()

# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)
#     drink_potion()
#
# #drink_potion() #NameError: name 'drink_potion' is not defined
# game()

#another 1
# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0] #Global Scope
#
# print(new_enemy)

#But

# def create_enemy():
#     game_level = 3
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]  # Global Scope
#
#     print(new_enemy)

#print(new_enemy) #NameError: name 'new_enemy' is not defined

"""Modifying a global a scope using return"""

# enemies = 1
#
# def increase_enemies():
#     print(f"Enemies inside function: {enemies}")
#     return enemies + 1
#
# enemies = increase_enemies()
# print(f"Enemies outside function: {enemies}")

"""#Global Variable/ Constant"""
#pi = 3.14159 #wrong
PI = 3.14159 #right

def calc():
    PI