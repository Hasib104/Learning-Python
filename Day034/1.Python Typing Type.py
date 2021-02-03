
"""#definig the type in the start"""
age:int
name:str
height:float
is_human:bool

#so that when we assign its value it will expect the expected type

def police_check(age: int) -> bool: #specifying the return type to bool using ->
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

print(police_check(12))

if police_check(19):
    print("You may pass.")
else:
    print("Pay a fine.")