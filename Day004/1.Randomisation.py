"""#Importing Module"""
# import my_module
# print(my_module.pi)


import random
"""#Random Generator"""
# random_int = random.randint(1, 100)
# print(random_int)

"""#Manipulating result of random generator using seed"""
# random.seed(8)
# random_int = random.randint(1, 10)
# print(random_int)

"""#Heads or Tail"""
test_seed=int(input("Enter a seed number: "))
print(test_seed)
random.seed(test_seed)
flip= random.randint(0, 1)
print(flip)
if flip == 1:
    print("Heads")
else:
    print("Tail")


