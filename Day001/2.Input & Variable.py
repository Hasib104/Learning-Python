"""#Input"""
#input("What is your name?")
"""#print+input"""
#print("hello " + input("What is your name?") + "!")
#used \n for showing the result in the next line
#print("\nhello " + input("What is your name?")+ "!")

"""#Exercise"""
#length of your name
#print(len(input("what is your name?")))
#or
#L=input("What is your name?")
#print(L)
#print(len(L))
#or
name=input("What is your name?")
length=len(name)
print(length)
number=len(name)
new_length= str(number)
print("Hello " + name + "!" "Your name has " + new_length + " characters")

"""#swap using variable"""
#a=input("a: ")
#print(a)
#b=input("b: ")
#print(b)
#c=a
#a=b
#b=c
#print("a: " + a)
#print("b: " + b)

"""#Band Name Generator"""
city=input("Name of the city you grew up in: \n")
print(city)
pet=input("Name of your favourite genre: \n")
print(pet)
print("The name of your band could be " +city + " " +pet)
