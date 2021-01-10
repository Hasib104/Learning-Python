
print("Welcome to Blind Auction")

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount= bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount

    print(f"The winner is {bidder} with a bid of ${highest_bid}")

bids = {}
replay = False

while not replay:
    name = input("Enter your name?: ")
    print(name)
    price = int(input("How much do you want to bid?:$ "))
    print(price)

    bids[name] = price

    replay = input("Are there any other bidders? type 'yes' or 'no'.: ")
    print(replay)

    if replay == "no":
        replay = True
        find_highest_bidder(bids)
    elif replay == "yes":
        replay = False