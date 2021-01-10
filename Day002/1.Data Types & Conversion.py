"""#Data types"""
# print("Hello" [4])
# print("123" + "345")
"""#Integer"""
# print(123+345)

"""#Type Checking and Conversion"""
# num_char=len(input("what is your name?"))
# print("your name has" + num_char + "characters")
# print(num_char)
# print(type(num_char))
# new_num_char=str(num_char)
# print("your name has "+ new_num_char+ " characters")

print(70+ float(100.5))
print(str(70)+ str(100))

"""#Exercise"""
two_digit_number=input("Type a two digit number: ")
print(two_digit_number)
print(type(two_digit_number))
first_digit= two_digit_number [0]
second_digit= two_digit_number [1]
print("First Digit: " +first_digit)
print("Second Digit: " +second_digit)
print(type(first_digit))
print(type(second_digit))
modified_first_digit= int(first_digit)
modified_second_digit= int(second_digit)
print(type(modified_first_digit))
print(type(modified_second_digit))
result= modified_first_digit+modified_second_digit
print(result)
print("result of two digit number is: " + str(result))
