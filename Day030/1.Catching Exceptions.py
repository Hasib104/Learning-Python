
"""#FileNotFound"""
# with open("file.txt") as file:
#     file.read()

"""#KeyError"""
# a_dict = {"key": "value"}
# value = a_dict["non_existent_key"]

"""#IndexError"""
# fruit_list = ["Apple", "Banana", "Cherry"]
# fruit = fruit_list[3]

"""#TypeError"""
# text = "abc"
# print(text + 5)

"""#Catching 1 error FileNotFound"""
# try:
#     file = open("file1.txt")
#
# except:
#     file = open("file1.txt", "w")
#     file.write("something")

"""#Catching multiple errors"""

# try:
#     file = open("file1.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["non_existent_key"])
# except FileNotFoundError:
#     file = open("file1.txt", "w")
#     file.write("something")
# # except KeyError:
# #     print("This key doesnt exist")
# except KeyError as error_message:
#     print(f"{error_message} doesnt exist")

"""#else"""

# try:
#     file = open("file1.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("file1.txt", "w")
#     file.write("something")
# # except KeyError:
# #     print("This key doesnt exist")
# except KeyError as error_message:
#     print(f"{error_message} doesnt exist")
# else:
#     content = file.read()
#     print(content)

"""#finally"""
# try:
#     file = open("file1.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["sdaskey"])
# except FileNotFoundError:
#     file = open("file1.txt", "w")
#     file.write("something")
# # except KeyError:
# #     print("This key doesnt exist")
# except KeyError as error_message:
#     print(f"{error_message} doesnt exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file was closed")

"""#Raising own exception"""

# try:
#     file = open("file1.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["sdaskey"])
# except FileNotFoundError:
#     file = open("file1.txt", "w")
#     file.write("something")
# # except KeyError:
# #     print("This key doesnt exist")
# except KeyError as error_message:
#     print(f"{error_message} doesnt exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file was closed")
#
#     raise TypeError("This is an self made error.")

#proper example

# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human height cant be over 3 metres.")
#
# bmi = weight / height ** 2
# print(bmi)

"""#Exercise"""
#4.1
# fruits = ["Apple", "Pear", "Orange"]
#
# def make_pie(index):
    # Use try: in that line of code where the error will occur.
#     try:
#         fruit = fruits[index]
#     except IndexError: #objective was just to run the code without any errors, no solution, just run the code
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
# make_pie(4)

#5.1
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    ### Use try: in that line of code where the error will occur.
    try:
        total_likes = total_likes + post['Likes']
    except KeyError: #just pass
        pass
        #or
        #total_likes += 0

print(total_likes)