import unittest
import random
from card import Card

class TestCard(unittest.TestCase):
    """Tests the shuffle method for ranks"""
    def test_shuffle_ranks(self):
        result = [Card.ranks]
        expected_result = [Card.ranks]
        random.shuffle(expected_result)
        self.assertCountEqual(result, expected_result)

    """Tests the shuffle method for suits"""
    def test_shuffle_suits(self):
        result = [Card.suits]
        expected_result = [Card.suits]
        random.shuffle(expected_result)
        self.assertCountEqual(result, expected_result)
    
    """Tests if the card value from value method matches the expected result and it is an integer"""
    def test_value(self):
        card = Card()
        result = card.value("Two of Hearts")
        expected_result = 2
        self.assertEqual(result, expected_result)
        self.assertIsInstance(result, int)
    
    """Tests the whole class"""
    def test_class(self):
        card = Card()
        self.assertIsInstance(card, Card)

    """Tests the value method if it throws an error if the input is not string"""
    def test_value_error(self):
        card = Card()
        self.assertRaises(AttributeError, card.value,1)
    
    """Tests the random_card method to make sure the returned result comes from ranks and suits lists in the right order """
    def test_random_card(self):
        card = Card()
        result = card.random_card()
        self.assertIsInstance(result, str)
        result_rank = result.split(" of ")[0]
        result_suit = result.split(" of ")[1]
        self.assertIn(result_rank, card.ranks)
        self.assertIn(result_suit, card.suits)    

if __name__ == '__main__':
    unittest.main()
