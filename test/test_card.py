"""Tests functionalities of the Card class."""


import unittest
import random
from war import card


class TestCard(unittest.TestCase):
    """Unit tests for Card class."""

    def test_shuffle_ranks(self):
        """Tests the shuffle method for ranks."""
        result = [card.Card.ranks]
        expected_result = [card.Card.ranks]
        random.shuffle(expected_result)
        self.assertCountEqual(result, expected_result)

    def test_shuffle_suits(self):
        """Tests the shuffle method for suits."""
        result = [card.Card.suits]
        expected_result = [card.Card().suits]
        random.shuffle(expected_result)
        self.assertCountEqual(result, expected_result)

    def test_value(self):
        """Tests if the card value from value method matches\
            the expected result and it is an integer."""
        card.Card()
        result = card.Card().value("Two of Hearts")
        expected_result = 2
        self.assertEqual(result, expected_result)
        self.assertIsInstance(result, int)

    def test_class(self):
        """Tests the whole class."""
        test_card = card.Card()
        self.assertIsInstance(test_card, card.Card)

    def test_value_error(self):
        """Tests the value method if it throws an error\
            if the input is not string."""
        card.Card()
        self.assertRaises(AttributeError, card.Card().value, 1)

    def test_random_card(self):
        """Makes sure that the returned result comes from\
            ranks and suits lists in the right order."""
        card.Card()
        result = card.Card().random_card()
        self.assertIsInstance(result, str)
        result_rank = result.split(" of ")[0]
        result_suit = result.split(" of ")[1]
        self.assertIn(result_rank, card.Card().ranks)
        self.assertIn(result_suit, card.Card().suits)

if __name__ == "__main__":
    unittest.main()
