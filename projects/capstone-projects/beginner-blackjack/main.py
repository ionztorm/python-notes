"""Blackjack Game."""

import os
import secrets

from art import logo

user_options = ["y", "n"]


def clear() -> None:
    """Clear the console screen."""
    os.system("cls" if os.name == "nt" else "clear")  # nosec  # noqa: S605


def deal_card(num_cards: int = 1) -> list[int]:
    """Deal a hand of blackjack.

    Args:
        num_cards (int): The number of cards to return.

    Returns:
        list[int]: A list of cards.

    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_list = []
    for _ in range(num_cards):
        card_list.append(secrets.choice(cards))
    return card_list


def check_blackjack(deck: list[int]) -> bool:
    """Check if the deck is a blackjack hand.

    Args:
        deck (list[int]): A deck of cards as a list

    Returns:
        bool: The deck is a blackjack hand, true or false.

    """
    return sum(deck) == 21 and len(deck) == 2


def display_winner(player_deck: list[int], dealer_deck: list[int]) -> None:
    """Display the outcome of the game."""
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


def check_is_score_over(deck: list[int]) -> bool:
    """Check if the deck is over 21.

    Args:
        deck (list[int]): A deck of cards.

    Returns:
        bool: The deck totals over 21, true or false.

    """
    if sum(deck) > 21:
        if 11 in deck:
            deck[deck.index(11)] = 1
            return sum(deck) > 21
        return True
    return False


def validate_dealer_deck(dealer_deck: (list[int])) -> None:
    """Validate the dealer's deck to ensure it has a score of at least 17.

    Args:
        dealer_deck (list[int]): A list of the dealers cards.

    """
    while sum(dealer_deck) < 17:
        dealer_deck.extend(deal_card(1))


def validate_user_input(user_input: str, input_options: list) -> str:
    """Validate user input to ensure it matches one of the valid options.

    Args:
        user_input (str): The initial input provided by the user.
        input_options (list[str]): A list of valid input options.

    Returns:
        str: The validated input, guaranteed to be one of the valid options.

    Raises:
        ValueError: If input_options is not a list of strings or user_input is not a string.

    """
    if not isinstance(user_input, str):
        raise ValueError("user_input must be a string.")
    if not isinstance(input_options, list) or not all(
        isinstance(option, str) for option in input_options
    ):
        raise ValueError("input_options must be a list of strings.")

    input_options_str = ",".join(input_options)

    validated_input = user_input
    while validated_input not in input_options:
        validated_input = input(
            f"Invalid input. Please try again. Valid inputs are {input_options_str}:\n"
        )
    return validated_input


def start_game() -> None:
    """Start a game of Blackjack."""
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


def check_should_start_game() -> None:
    """Check if the user wants to play a game. Collects user response via input."""
    play_game = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n':\n"
    ).lower()
    play_game = validate_user_input(play_game, user_options)

    if play_game == "y":
        start_game()
    else:
        print("Goodbye!")


check_should_start_game()
