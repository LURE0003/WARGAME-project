"""Class outputs random cards and finds their value."""

import random


class Card:
    """Class Card to shuffle card and get their value."""

    suits = ["Hearts", "Clubs", "Spades", "Diamonds"]

    ranks = [
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]

    values = {
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
        "Six": 6,
        "Seven": 7,
        "Eight": 8,
        "Nine": 9,
        "Ten": 10,
        "Jack": 11,
        "Queen": 12,
        "King": 13,
        "Ace": 14,
    }

    def random_card(self):
        """Draws a random card from list ranks and suits and returns the value as a string."""
        random.shuffle(self.ranks)
        random.shuffle(self.suits)
        return self.ranks[0] + " of " + self.suits[0]

    def value(self, value):
        """Returns the value of cards from the string created on random_card function."""
        return self.values.get(value.split(" of ")[0])
