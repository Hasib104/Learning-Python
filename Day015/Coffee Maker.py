
print("Welcome to Coffee Maker")

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

total_earned = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resource_checker(flavor):

    for item in flavor:
        if resources[item] < flavor[item]:
            print(f"Sorry not enough {item}")
            end_state = True
            return end_state
        else:
            end_state = False
            return end_state

def calculation(flavor):

    quarter_no = float(input("How many quarters?: "))
    dime_no = float(input("How many dimes?: "))
    nickel_no = float(input("How many nickels?: "))
    pennies_no = float(input("How many pennies?: "))

    total_coins_entered = round((quarter_no * 0.25) + (dime_no * 0.10) + (nickel_no * 0.05) + (pennies_no * 0.01), 2)
    return total_coins_entered

def coffee_maker(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


end_state = False

while not end_state:

    choice = input("What would you like to have? (espresso/latte/cappuccino): ")
    print(choice)

    if choice == "report":
        print(f"Water: {resources['water']}ml.")
        print(f"Milk: {resources['milk']}ml.")
        print(f"Coffee: {resources['coffee']}ml.")
        print(f"Money: ${total_earned}.")
    elif choice == "off":
        end_state = True
    else:
        chosen_flavor = MENU[choice]
        print(chosen_flavor)
        if resource_checker(chosen_flavor["ingredients"]) == False:
            paid = calculation(chosen_flavor)
            print(f"You have paid ${paid} in coins.")
            if paid >= chosen_flavor["cost"]:
                total_earned += chosen_flavor["cost"]
                returned = round((paid - chosen_flavor["cost"]), 2)
                coffee_maker(choice, chosen_flavor["ingredients"])
                print(f"Here is your change ${returned}.")
            else:
                print(f"Sorry you haven't paid enough money.")
                end_state = True
        else:
            print("Sorry not enough resources to complete the order.")
            end_state = True