import random

"""#Jumping Obstacle using while loop"""
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Ffreeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle1.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# obs_to_jump=int(input("How many is there? "))
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# while obs_to_jump > 0:
#     jump()
#     obs_to_jump -= 1
#     print(obs_to_jump)


"""#Jumping Obstacle with final goal random"""
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Ffreeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle2.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# r_goal= random.randint(0,4)
# print(r_goal)
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# def at_goal():
#     print("You have reached the end point")
#
# step = 0
# while step != r_goal:
#     jump()
#     step+=1
# at_goal()

"""#Hurdle 3"""
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Ffreeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

"""#Hurdle 4"""
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Ffreeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_right()
    turn_left()
def go_up():
    turn_left()
    move()
    turn_right()
def look_down():
    turn_right()
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        while wall_in_front():
            go_up()
        jump()
        look_down()
        while not wall_in_front():
            move()
        turn_left()


"""#Escaping the maze"""
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()

    elif right_is_clear():
        turn_right()
        move()

    else:
        turn_left()