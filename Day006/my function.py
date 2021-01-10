def my_function():
    print("Hello")
    print("I am Hasib")

my_function()


"""#Turn right and come back to 00"""
#go to reborgs world
def turn_right():
    turn_left()
    turn_left()
    turn_left()

turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()


"""#obstacle jump"""
#go to reborgs world
def turn_right():
    turn_left()
    turn_left()
    turn_left()

obs_to_jump=int(input("How many is there? "))
for obstacle in range(0, obs_to_jump):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

