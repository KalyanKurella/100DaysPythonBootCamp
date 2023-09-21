import os
from art import logo
print(logo)
more_Bidders = True
bids = {}
def find_highest_bid(dict):
    highest_bid = 0
    bidder_name =""
    for name in dict :
        value = int(dict[name])
        if value > highest_bid :
            highest_bid = value
            bidder_name = name
        else :
            pass
    print(f"The highest is of {bidder_name} of bid {highest_bid}")

while(more_Bidders):
    name = input("What is your name? ")
    bid_amount = input()
    bids[name] = bid_amount
    check = input("enter yes if there is any other bidder else no : ")
    if check == "yes":
        more_Bidders = True
        os.system('cls')
    else :
        more_Bidders = False
find_highest_bid(bids)