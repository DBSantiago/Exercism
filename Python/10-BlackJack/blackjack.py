"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    """
    card_letters = ["A", "K", "Q", "J"]

    value = 0

    if card not in card_letters:
        value = int(card)
    elif card.upper() == "A":
        value = 1
    else:
        value = 10

    return value


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """
    highest_card = card_one

    if value_of_card(card_one) < value_of_card(card_two):
        highest_card = card_two
    elif value_of_card(card_one) == value_of_card(card_two):
        highest_card = (card_one, card_two)

    return highest_card


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. 'J', 'Q', 'K' = 10;
           'A' = 11 (if already in hand); numerical value otherwise.

    :return: int - value of the upcoming ace card (either 1 or 11).
    """
    if "A" in (card_one, card_two):
        ace_value = 1
    else:
        if value_of_card(card_one) + value_of_card(card_two) > 10:
            ace_value = 1
        else:
            ace_value = 11
    return ace_value


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 11; numerical value otherwise.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """
    blackjack = False
    cards_10_value = ["K", "Q", "J", "10"]

    if "A" in (card_one, card_two) and ("A", "A") != (card_one, card_two):
        if card_one in cards_10_value or card_two in cards_10_value:
            blackjack = True

    return blackjack


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """

    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """
    double_down_values = [9, 10, 11]
    return value_of_card(card_one) + value_of_card(card_two) in double_down_values
