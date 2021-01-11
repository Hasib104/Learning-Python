
import random
print("Welcome to Guess the number.")
print("I am thinking of a number between 1 and 100.")

numbers=[]
for counter in range(0,101):
    numbers.append(counter)
#print(numbers)

def select_number():
    chosen_number = random.choice(numbers)
    return chosen_number

lives_easy = 10
lives_hard = 5

chosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

def difficulty_chose(difficulty):
    if difficulty == "easy":
        return lives_easy
    elif difficulty == "hard":
        return lives_hard
    else:
        return 0

def guess_number():
    total_lives = difficulty_chose(chosen_difficulty)
    print(f"You have {total_lives} attempts to guess the number.")
    end_state = False
    chosen_number = select_number()
    print(chosen_number)

    while not end_state:

        for lives in range(0, total_lives):
            guess_number = int(input("Make a guess: "))

            if guess_number == chosen_number:
                end_state = True
                print("You have guessed the number.")
                return
            elif guess_number > chosen_number:
                total_lives -= 1
                print("Too High")
                print(f"Lives remaining {total_lives}")
            elif guess_number < chosen_number:
                total_lives -= 1
                print("Too Low")
                print(f"Lives remaining {total_lives}")
            if total_lives == 0:
                end_state = True
                print("You have ran out of lives")
                return

guess_number()