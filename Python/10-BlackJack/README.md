# Instructions

In this exercise you are going to implement some rules of Blackjack, such as the way the game is played and scored.

Note : In this exercise, _A_ means ace, _J_ means jack, _Q_ means queen, and _K_ means king. Jokers are discarded. A standard French-suited 52-card deck is assumed, but in most versions, several decks are shuffled together for play.

## 1. Calculate the value of a card

In Blackjack, it is up to each individual player if an ace is worth 1 or 11 points (more on that later). Face cards (J, Q, K) are scored at 10 points and any other card is worth its "pip" (numerical) value.

Define the value_of_card(< card >) function with parameter card. The function should return the numerical value of the passed-in card string. Since an ace can take on multiple values (1 or 11), this function should fix the value of an ace card at 1 for the time being. Later on, you will implement a function to determine the value of an ace card, given an existing hand.

## 2. Determine which card has a higher value

Define the higher_card(<card_one>, <card_two>) function having parameters card_one and card_two. For scoring purposes, the value of J, Q or K is 10. The function should return which card has the higher value for scoring. If both cards have an equal value, return both. Returning both cards can be done by using a comma in the return statement.

An ace can take on multiple values, so we will fix _A_ cards to a value of 1 for this task.

## 3. Calculate the value of an ace

As mentioned before, an ace can be worth either 1 or 11 points. Players try to get as close as possible to a score of 21, without going over 21 (going "bust").

Define the value_of_ace(< card_one >, < card_two >) function with parameters card_one and card_two, which are a pair of cards already in the hand before getting an ace card. Your function will have to decide if the upcoming ace will get a value of 1 or a value  of 11, and return that value. Remember: the value of the hand with the ace needs to be as high as possible without going over 21.

Hint: if we already have an ace in hand then its value would be 11.
