"""Tests functionalities of the game class."""


import unittest
import unittest.mock
import io
import random
import sys
import os
from war import game


class test_game(unittest.TestCase):
    """Unit tests for the game class."""

    class HiddenPrints:
        """This class is used to hide the print outputs."""

        def __enter__(self):
            """Doesn't allow print statements."""
            self._original_stdout = sys.stdout
            sys.stdout = open(os.devnull, "w")

        def __exit__(self, exc_type, exc_val, exc_tb):
            """Allows to print after exiting."""
            sys.stdout.close()
            sys.stdout = self._original_stdout

    def test_init(self):
        """Tests if the class exists."""
        res = game.Game()
        exp = game.Game
        self.assertIsInstance(res, exp)

    def test_wins(self):
        """Tests if the correct output will occur when the player wins."""
        with self.HiddenPrints():
            res = game.Game().who_wins(1, 1, 0, 2)
            exp = (None, 2, 0)
            self.assertEqual(res, exp)

    def test_loss(self):
        """Tests if the correct output will occur when the player loses."""
        with self.HiddenPrints():
            res = game.Game().who_wins(1, 1, 2, 0)
            exp = (None, 0, 2)
            self.assertEqual(res, exp)

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        """Catches the "print" output."""
        game.Game().print_screen(n, 1, 1)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_print_true(self):
        """Tests if the print function delivers the correct output when\
            the player wins."""
        exp = "Great! You win!!!\nYou have 1 cards and the computer has 1\n"
        self.assert_stdout(True, exp)

    def test_print_false(self):
        """Tests if the print function delivers the correct output when\
            the player loses."""
        exp = "The computer wins!!!\nYou have 1 cards and the computer has 1\n"
        self.assert_stdout(False, exp)

    def test_war(self):
        """Tests if a war occurs correctly."""
        random.seed(0)
        with self.HiddenPrints():
            test_game = game.Game().war(5, 5)
            if test_game == (None, 9, 1) or test_game == (None, 1, 9):
                res = True
            else:
                res = False
            exp = True
            self.assertEqual(res, exp)

    def test_input_cheat(self):
        """Tests if the player can cheat"""
        with unittest.mock.patch("builtins.input", return_value="cheat"):
            res = game.Game().ask_input()
            exp = True
        self.assertEqual(res, exp)

    def test_input_yes(self):
        """Tests if the function will accept yes for an answer."""
        with unittest.mock.patch("builtins.input", return_value="yes"):
            res = game.Game().ask_input()
            exp = True
            self.assertEqual(res, exp)

    def test_input_no(self):
        """Tests if the function will accept no for an answer."""
        with unittest.mock.patch("builtins.input", return_value="no"):
            res = game.Game().ask_input()
            exp = False
            self.assertEqual(res, exp)

    def test_cheat_short(self):
        """Tests if playing the short version is possible."""
        with self.HiddenPrints():
            game.Game().play_short("Tester", cheat=True)
            res = True
            with open("highscores_short.txt", "r") as r:
                if "Tester" in " ".join(r.readlines()):
                    exp = True
                else:
                    exp = False
            self.assertEqual(res, exp)

    def test_short(self):
        """Tests if short will end when answer is no"""
        with self.HiddenPrints():
            with unittest.mock.patch("builtins.input", return_value="no"):
                game.Game().play_short("Tester")
                exp = True
                with open("highscores_short.txt", "r") as r:
                    if "26" in " ".join(r.readlines()):
                        res = True
                    else:
                        res = False
                self.assertEqual(res, exp)

    def test_long(self):
        """Tests if long will end when answer is no"""
        with self.HiddenPrints():
            with unittest.mock.patch("builtins.input", return_value="no"):
                game.Game().play_long("Tester")
                exp = True
                with open("highscores_long.txt", "r") as r:
                    if "26" in " ".join(r.readlines()):
                        res = True
                    else:
                        res = False
                self.assertEqual(res, exp)

    def test_cheat_long(self):
        """Tests if playing the long version is possible."""
        with self.HiddenPrints():
            game.Game().play_long("Tester", cheat=True)
            res = True
            with open("highscores_long.txt", "r") as r:
                if "Tester" in " ".join(r.readlines()):
                    exp = True
                else:
                    exp = False
            self.assertEqual(res, exp)
