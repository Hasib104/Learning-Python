
#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


import random

def deal_card():
    cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    chosen_card = random.choice(cards_deck)
    return chosen_card

def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "You lost, Dealer has Blackjack."
    elif user_score == 0:
        return "You won with a Blackjack."
    elif user_score > 21:
        return "You lost, you went over 21."
    elif dealer_score > 21:
        return "You won, dealer went over 21."
    elif user_score > dealer_score:
        return "You won"
    else:
        return "You lost"

user_card = []
dealer_card = []

for counter in range(0, 2):
    user_card += [deal_card()]  #if we change the chosen_card(int) to list by adding [] to assign the value it will not show an error as TypeError: 'int' object is not iterable
    dealer_card.append(deal_card())

end_game = False

while not end_game:

    user_score = calculate_score(cards=user_card)
    dealer_score = calculate_score(cards=dealer_card)
    print(f"Your cards: {user_card} score: {user_score}")
    print(f"Dealer cards: {dealer_card[0]}")

    if user_score > 21 or dealer_score == 0 or user_score == 0:
        end_game = True
    else:
        decision = input("Type 'y' to get another card, Type 'n' to pass: ")

        if decision == "y":
            user_card.append(deal_card())
        else:
            end_game = True

while dealer_score != 0 and dealer_score < 17:
    dealer_card.append(deal_card())
    dealer_score = calculate_score(dealer_card)

print(compare(user_score, dealer_score))