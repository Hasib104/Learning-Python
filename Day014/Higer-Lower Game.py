
import random
import art
import game_data
print(art.logo)

def first_randomiser():

    chosen_one = {}
    chosen_one = random.choice(game_data.data)
    print(f"Compare A: {chosen_one['name']}, {chosen_one['description']}, from {chosen_one['country']}")
    A = chosen_one
    score = 0

    end_state = False
    while not end_state:

        print(art.vs)

        chosen_two = {}
        chosen_two = random.choice(game_data.data)
        print(f"Against B: {chosen_two['name']}, {chosen_two['description']}, from {chosen_two['country']}")
        B = chosen_two

        decision = input("Who has more followers? Type 'A' or 'B': ")
        print(decision)

        if decision == "A":
            if A['follower_count'] > B['follower_count']:
                score += 1
                print(f"You Won This Round. Your Score is: {score}")
                print(f"Compare A: {chosen_one['name']}, {chosen_one['description']}, from {chosen_one['country']}")

            else:
                print(f"You Lose. Your Score is: {score}")
                end_state = True
                return


        elif decision == "B":
            if B['follower_count'] > A['follower_count']:
                B = A
                score += 1
                print(f"You Won This Round. Your Score is: {score}")
                print(f"Compare A: {chosen_two['name']}, {chosen_two['description']}, from {chosen_two['country']}")

            else:
                print(f"You Lose. Your Score is: {score}")
                end_state = True
                return

first_randomiser()
