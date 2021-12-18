# for key in data: # Iterates just through the keys, ignoring the values
# for key, value in d.items(): # Iterates through the pairs
# for key in d.keys(): # Iterates just through key, ignoring the values
# for value in d.values(): # Iterates just through value, ignoring the keys
# https://stackoverflow.com/a/8381589


print("Welcome to the silent auction program.")

results = {}


def auction(name, bid):
    results[name] = bid
    auction.winning_bid = max(results.values())
    auction.winner = max(results, key=results.get)


rerun = True
while rerun is True:

    name = input("What is your name? ").lower()
    bid = int(input("What is your bid? $"))

    confirm_rerun = input(
        "Will someone else be bidding? Type 'yes' or 'no.' \n"
    ).lower()

    if confirm_rerun == "no":
        print(
            f"The winner is {auction.winner} with a bid of"
            f" ${auction.winning_bid}."
        )
        rerun = False

    auction(name, bid)

# Differences in her code:
# While loop is `while not bidding_finished`
# Normally she seems to avoid negative statements like this?
# Has bids[name] = price inside while statement
# def find_highest_bidder(bidding_record):
#     highest_bid = 0
#     for bidder in bidding_records:
#         bid_amount = bidding_record[bidder]  # returns value of a key
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winnder is {winner} with a bid of {highest_bid}.")
