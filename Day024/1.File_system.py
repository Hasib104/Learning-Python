
"""#Reading a file"""
#this method takes lots of resources from computer
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()


#advised method for file opening, this method doesn't require file.close()
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

"""#Writing a file"""
# #replaces existing contents
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")

#appends with existing contents
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

"""#Absolute path"""
# with open("C:/Users/Merc/Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

"""#Realtive path"""
with open("../../../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)