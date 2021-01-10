
"""#Function with outputs"""

# def format_name(f_name, l_name):
#
#     print(f_name + " " + l_name)
#
# f_name = input("Enter First name: ").title()
# l_name = input("Enter Last name: ").title()
# format_name(f_name, l_name)

#Or

# def format_name(f_name, l_name):
#
#     formated_f_name= f_name.title()
#     formated_l_name = l_name.title()
#     print(f"{formated_f_name} {formated_l_name}")
#
# f_name = input("Enter First name: ")
# l_name = input("Enter Last name: ")
# format_name(f_name, l_name)

"""#Retruning value using return function"""

# def format_name(f_name, l_name):
#
#     formated_f_name= f_name.title()
#     formated_l_name = l_name.title()
#     return (f"{formated_f_name} {formated_l_name}")
#
# f_name = input("Enter First name: ")
# l_name = input("Enter Last name: ")
# print(format_name(f_name, l_name))

"""End the program early with return instead of running the whole code"""

# def format_name(f_name, l_name):
#
#     if f_name == "" or l_name == "":
#         return "\nPlease provide First and Last name."
#     else:
#         formated_f_name= f_name.title()
#         formated_l_name = l_name.title()
#         return (f"{formated_f_name} {formated_l_name}")
#
# f_name = input("Enter First name: ")
# l_name = input("Enter Last name: ")
# print(format_name(f_name, l_name))


"""#Leap year with return"""
print("Welcome to Leap Year Calculator")

def is_leap():
    if year%4 == 0 and year%100 == 0 and year%400 == 0 :
        return True
    elif year%4 == 0 and year%100 != 0 and year%400 != 0 :
        return True
    elif year%4 == 0 and year%100 == 0 and year%400 != 0 :
        return False
    else:
        return False

def days_in_month(year, month):

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap() == True:
        return 29
    elif month > 12 or month < 1:
        return "invalid month"
    else:
        return month_days[month -1]

year = int(input("Input a year: "))
print(year)
month = int(input("Input a month of the year: "))
print(month)
days = days_in_month(year, month)
print(days)
