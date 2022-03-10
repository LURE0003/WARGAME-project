"""Shell class for the game."""
import cmd
from war import game


class Shell(cmd.Cmd):
    """Shell for war game."""

    def __init__(self, name):
        """Class constructor, prints out commands."""
        super(Shell, self).__init__()
        print("""Type 'start', 'long', 'changename', 'exit' or 'help'""")
        self.name = name

    def do_start(self, _):
        """Start the game in "short" mode with "cheat" off."""
        print("""
You and me will play war game.
When you want to draw a card, press enter.
Whoever has a higher card win both cards.
If we have the same card value, a war will start!\n""")
        the_game = game.Game()
        the_game.play_short(self.name)
        print("""\nType 'start' to start a new game or 'exit' to quit.""")

    def do_long(self, _):
        """Start the game in "long" mode with "cheat" off."""
        print("""This is a long version of the game.
        We will play until one of us has all of the deck.
        When you want to draw a card, press enter.""")
        long_game = game.Game()
        long_game.play_long(self.name)
        print("""\nType 'long' to start a new game or 'exit' to quit.\n""")

    def do_exit(self, _):
        """Exit the game."""
        print("""\nThank you for playing with me! Bye!\n""")
        return True

    def do_restart(self, _):
        """Restarts the game."""
        print("""You chose to restart the game.""")
        self.do_start(_)

    def do_cheat(self, _):
        """Plays the game in cheat mode, short."""
        print("""Cheater!""")
        cheat_game = game.Game()
        cheat_game.play_short("Cheater", cheat=True)

    def do_longcheat(self, _):
        """Plays the game in cheat mode, long."""
        print("""Cheater!""")
        cheat_game = game.Game()
        cheat_game.play_long("Cheater", cheat=True)

    def do_changename(self, _):
        """Change the players name."""
        name = input("Please enter a name: ")
        self.name = name
