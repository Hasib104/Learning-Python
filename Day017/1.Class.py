
"""#Creating a custom class"""
# class User:
#     pass
#
# user_1 = User()
#
# def function():
#     pass
#
# print("Hello")
#
"""#Adding attribute to the object"""

# user_1.id = "001"
# user_1.username = "Hasib"
#
# print(user_1.username)

"""#Create a constructor"""

# class User:
#     def __init__(self):
#         print("New user being created...") #gets print everytime the class is used
#
# user_1 = User()
# user_1.id = "001"
# user_1.username = "Hasib"
#
# print(user_1.username)
#
# user_2 = User()
# user_2.id = "002"
# user_2.username = "Kamal"
#
# print(user_2.username)

"""#Adding value in constructor"""

# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0 #Setting a default value
#
#
# user_1 = User("001", "Hasib")
#
# print(user_1.id)
# print(user_1.username)
# print(user_1.followers)

# user_2 = User()
# user_2.id = "002"
# user_2.username = "Kamal"
#
# print(user_2.username)

"""#Adding Methods"""

# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0 #Setting a default value
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
# user_1 = User("001", "Hasib")
# user_2 = User("002", "Inesa")
#
# user_1.follow(user_2) #user_1 following user_2
#
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)

"""#Exercise"""