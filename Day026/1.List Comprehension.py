
"""#Creating a list from another list"""
#Using for loop
# numbers = [1,2,3]
# new_list = []
# for n in numbers:
#     add_1 = n+1
#     new_list.append(add_1)
# print(new_list)

#Using List Comprehension
#Structure
#new_list = [new_item for item in list]

# new_list = [n + 1 for n in numbers]
# print(new_list)
#
# name = "Angela"
# letter_list = [letter for letter in name]
# print(letter_list)

# range_list = [item*2 for item in range(1,5)]
# print(range_list)

"""#Conditional list comprehension"""
#Structure
# new_list = [new_item for item in list if test]
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
#
# long_names_uppercase = [name.upper() for name in names if len(name) > 5]
# print(long_names_uppercase)

"""#Exercise"""
#3.1
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [item**2 for item in numbers]
# print(squared_numbers)

#4.1
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [item for item in numbers if item % 2 == 0]
# print(result)

#5.1
# with open("file1.txt") as file1:
#     file1_data = file1.readlines()
#
# with open("file2.txt") as file2:
#     file2_data = file2.readlines()
#
# result = [int(num) for num in file1_data if num in file2_data]
# print(result)

