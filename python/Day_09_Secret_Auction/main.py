import artwork

def secret_auction():
    bids={}
    while True:
        name = input("\nPlease enter your name: ")
        bid = int(input("\nPlease enter your bid: $"))
        bids[name]=bid
        if input("\nIs there another bidder (Enter yes or no): ").lower()=="no":
            break

    highest_bid = 0
    highest_bidder = ""
    for key, value in bids.items():
        if value > highest_bid:
            highest_bid = value
            highest_bidder = key

    print(f"\nThe winner is {highest_bidder} with a bid of ${highest_bid}")

print(artwork.hammer,artwork.logo)


secret_auction()
