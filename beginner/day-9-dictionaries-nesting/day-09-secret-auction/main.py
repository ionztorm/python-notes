import os


bids = {}
repeat = True


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def get_highest_bid(bids):

    all_bids = bids.copy()
    highest_bid = 0
    highest_bidder = ""

    for bid in all_bids:
        for bidder, bid in all_bids.items():
            if bid > highest_bid:
                highest_bid = bid
                highest_bidder = bidder

    return highest_bidder, highest_bid


while repeat:
    name = input("What is your name?: \n")
    price = int(input("What is your bid?: \n£"))
    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n"
    ).lower()

    bids[name] = price

    if should_continue == "no":
        repeat = False
        clear()
    else:
        clear()

winner, with_bid = get_highest_bid(bids)

print(f"The winner is {winner} with a bid of £{with_bid}.")
