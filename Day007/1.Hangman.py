import random
import Hangman_logo
import Hangman_words
import Hangman_pics

HANGMANPICS= Hangman_pics.HANGMANPICS
logo = Hangman_logo.logo
print(logo)
words_list = Hangman_words.words_list
#print(words_list)
chosen_word= random.choice(words_list)
#print(chosen_word)
chosen_word_length = len(chosen_word)
print(f"Chosen word has {chosen_word_length} letters.")

# guess_letter = input("Enter a letter that might be in the word: \n").lower()

guess=[]
display= []

#challenge 1

# for x in chosen_word:
#     if guess_letter == x:
#         print("right")
#     else:
#         print("wrong")

#challenge 2

for letter in range(0, chosen_word_length):
    display += "_"
print(display)

#replacing value in a list using index
#
# for n in range(0, chosen_word_length):
#     letter_replace = chosen_word[n]
#     if guess_letter == letter_replace:
#         display[n] = letter_replace
#
# print(display)
# print(len(display))
# print(type(display))
# print(chosen_word)
# print(type(chosen_word))

#challenge 3

# end_of_game = False
#
# while not end_of_game: #this loop execute until end goal
#     guess_letter = input("Enter a letter that might be in the word: \n").lower()
#
#     for n in range(0, chosen_word_length):
#         if guess_letter == chosen_word[n]:
#             display[n] = guess_letter
#             print(display)
#
#     if "_" not in display:   #checking if "_" is in display
#         end_of_game= True
#         print("You Win")
#
# print(display)


#challenge 4

end_of_game = False
lives = 6

while not end_of_game: #this loop execute until end goal
    guess_letter = input("Enter a letter that might be in the word: \n").lower()

    for n in range(0, chosen_word_length):
        if guess_letter == chosen_word[n]:
            display[n] = guess_letter
    print("You guessed right")
    print(display)

    if guess_letter not in chosen_word: #in function very useful
        lives-=1
        print("You guessed wrong")
        if lives == 0:
            end_of_game = True
            print("You Lose")

        print(f"Lives Reamaining {lives}")
        print(HANGMANPICS[lives])

    if "_" not in display:   #checking if "_" is in display
        end_of_game= True
        print("You Win")