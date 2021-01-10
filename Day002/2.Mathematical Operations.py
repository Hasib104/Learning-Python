# print(3+5)
# print(7-4)
# print(5*2)
# print(5**2)
# print(12/3)
# print(3*3+3/3-7)

"""#BMI Calculator"""
# height = float(input("enter your height in m: "))
# print(height)
# print(type(height))
# weight = int(input("enter your weight in kg: "))
# print(weight)
# print(type(weight))
# BMI=weight/height**2
# BMI_int= int(BMI)
# print("Result of BMI is: " + str (BMI_int))

"""#Round"""
# print(8/3)
# print(int(8/3))
# print(round(8/3))
# print(round(8/3, 2))

# result=4/2
# result/=2 #instead of result=result/2
# print(result)

# score=0
# score+=1 #instead of score=score+1
# score-=1 #....
# score*=1 #....
# score/=1 #....
# print(score)

"""#f-string"""
# score=0
# height=1.8
# iswinning= True
# print(f"your score is {score}, your height is {height}, your winning is {iswinning}")

"""#Life left"""
# life_expectancy_year= int(input("What is your life expectancy? "))
# print(life_expectancy_year)
# print(type(life_expectancy_year))
# life_expectancy_month= life_expectancy_year*12
# life_expectancy_weeks= life_expectancy_year*52
# life_expectancy_days= life_expectancy_year*365
#
# current_age_year= int(input("What is your current age? "))
# print(current_age_year)
# print(type(current_age_year))
# current_age_month= current_age_year*12
# current_age_weeks= current_age_year*52
# current_age_days= current_age_year*365
#
# years_left= life_expectancy_year-current_age_year
# months_left= life_expectancy_month-current_age_month
# weeks_left= life_expectancy_weeks-current_age_weeks
# days_left= life_expectancy_days-current_age_days
# print(f"You have {years_left} years, {days_left} days, {weeks_left} weeks, and {months_left} months left.")

"""#Tip Calculator"""
total_bill=float(input("What was the total bill? "))
print(total_bill)
tip_percentage=int(input("what percentage of tip you like to give? (10%, 12%, or 15%) "))
print(tip_percentage)
people= int(input("How many people to split the bill? "))
print(people)

total_bill_with_tip= round(total_bill+ total_bill*(tip_percentage/100), 2)
total_bill_per_person= round((total_bill_with_tip/people), 2)
print(f"Total bill ${total_bill_with_tip} tips included. \nEach person should pay ${total_bill_per_person}")

