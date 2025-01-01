import random
import os
from art import logo

user_options = ["y", "n"]


def clear():
    """Clear the console screen"""
    return os.system("cls" if os.name == "nt" else "clear")


def deal_card(num_cards=1):
    """Return a list of random cards. Accepts an optional argument to specify the number of cards to deal."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_list = []
    for _ in range(num_cards):
        card_list.append(random.choice(cards))
    return card_list


def check_blackjack(deck):
    """Check if the deck is a blackjack hand"""
    if sum(deck) == 21 and len(deck) == 2:
        return True
    else:
        return False


def display_winner(player_deck, dealer_deck):
    if check_blackjack(player_deck):
        print("You have Blackjack! You win!")
    elif check_blackjack(dealer_deck):
        print("Dealer has Blackjack! You lose!")
    elif check_is_score_over(player_deck):
        print("You went over. You lose!")
    elif check_is_score_over(dealer_deck):
        print("Dealer went over. You win!")
    elif sum(player_deck) > sum(dealer_deck):
        print("You win!")
    elif sum(player_deck) < sum(dealer_deck):
        print("You lose!")
    else:
        print("It's a draw!")


def check_is_score_over(deck):
    """Check if the deck is over 21"""
    if sum(deck) > 21:
        if 11 in deck:
            deck[deck.index(11)] = 1
            return sum(deck) > 21
        return True
    return False


def validate_dealer_deck(dealer_deck):
    """Validate the dealer's deck to ensure it has a score of at least 17"""
    while sum(dealer_deck) < 17:
        dealer_deck.extend(deal_card(1))


def validate_user_input(user_input, input_options):
    """Validate the user's input to ensure it is one of the valid options. Accepts the user's input and a list of valid options."""
    new_input = user_input
    input_options_str = ",".join(input_options)
    while new_input not in input_options:
        new_input = input(
            f"Invalid input. Please try again. Valid inputs are {input_options_str}:\n"
        )
    return new_input


def start_game():
    """Start a game of Blackjack"""
    clear()
    print(logo)
    game_is_over = False
    player_cards = deal_card(2)
    dealer_cards = deal_card(2)

    validate_dealer_deck(dealer_cards)

    while not game_is_over:
        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if (
            check_blackjack(player_cards)
            or check_blackjack(dealer_cards)
            or check_is_score_over(player_cards)
        ):
            game_is_over = True
        else:
            should_deal_card = input(
                "Do you want to draw another card? Type 'y' or 'n':\n"
            ).lower()
            should_deal_card = validate_user_input(should_deal_card, user_options)
            if should_deal_card == "y":
                player_cards.extend(deal_card(1))
            else:
                break

    print(f"\n\nYour cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Dealer's cards: {dealer_cards}, current score: {sum(dealer_cards)}")
    display_winner(player_cards, dealer_cards)
    check_should_start_game()


def check_should_start_game():
    play_game = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n':\n"
    ).lower()
    play_game = validate_user_input(play_game, user_options)

    if play_game == "y":
        start_game()
    else:
        print("Goodbye!")


check_should_start_game()
