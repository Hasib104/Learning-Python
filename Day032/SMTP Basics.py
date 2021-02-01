
"""#Basic SMTP"""
# import smtplib
#
# my_email = "hasib104.python@gmail.com"
# password = "Pp123456"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="hasibkamal14@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

"""#Datetime"""
# import datetime
#
# now = datetime.datetime.now()
# print(now)
# year = now.year
# print(year)
# month = now.month
# print(month)
# day_of_week = now.weekday()
# print(day_of_week)
#
# """#creating a object from datetime class"""
# date_of_birth = datetime.datetime(year=1996, month=6, day=29)
# print(date_of_birth)

"""#Sending Motivation Code"""
import datetime
import random
import smtplib

MY_EMAIL = "hasib104.python@gmail.com"
PASSWORD = "Pp123456"

now = datetime.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt", encoding="utf8") as quote_file: ###Need to add encoding "uft-8" so that ascii error doenst occur.
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs="hasibkamal14@gmail.com",msg=f"Subject:Hello\n\n{quote}".encode('utf-8')) ###Need to add encoding "uft-8" so that ascii error doenst occur.