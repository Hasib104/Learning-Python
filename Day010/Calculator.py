
print("Welcome to Basic Calculator")

def calculation():

    def calculator(f_value, l_value):
        if symbol == "+":
            return f_value + s_value
        elif symbol == "-":
            return f_value - s_value
        elif symbol == "*":
            return f_value * s_value
        elif symbol == "/":
            return f_value / s_value
        else:
            return "Invalid oprational symbol."

    f_value = float(input("Enter a value: "))
    print(f_value)

    end_state = False

    while not end_state:
        symbol = input("Pick an operational symbol.'+', '-', '*', '/'")
        print(f"Chosen operational symbol: {symbol}")
        s_value = float(input("Enter another value: "))
        print(s_value)

        result = calculator(f_value, s_value)
        print(f"Final result {result}")

        decision = input("Do you want to do more calculation? Types 'y' or 'n': ")
        if decision == "n":
            end_state = True
            print(f"Final result is {result}")
            calculation()

        elif decision == "y":
            f_value = result

calculation()