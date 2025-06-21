
def find_highest_bidder(bidding_dictionary):
    winner=""
    highest_bid=0
    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder


    print(f"the winner is {winner}with a bid of ${highest_bid} ")


bids={}
continue_biding=True
while continue_biding:
    name=input("whats your name ?")
    price=int(input("how much amount you want to bid"))
    bids[name]=price
    third_question=input("are there any other useres,type'yes'if not then type'no'\n").lower()
    if third_question=="no":
        continue_biding=False
        find_highest_bidder(bids)
    elif third_question=="yes":
        print("\n"*50)
    