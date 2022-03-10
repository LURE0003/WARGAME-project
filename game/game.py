"""The logic behind the War card game."""
from game import card
from game import highscores


class Game:
    """Placeholder for docstring."""
    cheat = False

    def play_short(self, player, cheat=False) -> None:
        """Plays the game for only 26 turns, shorter version."""
        com_cards, hum_cards = 26, 26

        for i in range(26):
            c = card.Card()
            print("\n" + "-" * 30)
            card_you, card_computer = c.random_card(), c.random_card()
            val_you, val_com = c.value(card_you), c.value(card_computer)
            print(f"You: {card_you:<8} | Computer: {card_computer}")
            if not cheat:
                if not self.ask_input():
                    break
            if val_you != val_com:
                res = self.who_wins(com_cards, hum_cards, val_com, val_you)
                hum_cards, com_cards = res[1], res[2]
            elif com_cards < 4 or hum_cards < 4:
                print("We don't have enough cards for war")
            else:
                res_two = self.war(com_cards, hum_cards)
                hum_cards, com_cards = res_two[1], res_two[2]
        if com_cards > hum_cards:
            print("\nYOU LOST. Maybe next time ;)")
        elif com_cards < hum_cards:
            print("\nYOU WIN!!! Congrats!")
        else:
            print("\nIt's a tie. No one wins.")
        print(f"\nFinal score:\nYou: {hum_cards} | Computer: {com_cards}")
        highscores.highscores().short_scores(
            player, hum_cards, hum_cards > com_cards)

    def play_long(self, player, cheat=False) -> None:
        """Plays the game until the entire deck runs out, long version."""
        """CAUTION: This can take more than 300 draws!"""
        com_cards, hum_cards, counter = 26, 26, 0

        while com_cards > 0 and hum_cards > 0:
            c = card.Card()
            print("\n" + "-" * 30)
            card_you, card_computer = c.random_card(), c.random_card()
            val_you, val_com = c.value(card_you), c.value(card_computer)
            print(f"You: {card_you:<8} | Computer: {card_computer}")
            if not cheat:
                if not self.ask_input():
                    break
            if val_you != val_com:
                res = self.who_wins(com_cards, hum_cards, val_com, val_you)
                hum_cards, com_cards = res[1], res[2]
            elif com_cards < 4 or hum_cards < 4:
                print("We don't have enough cards for war")
                counter -= 1
            else:
                res_two = self.war(com_cards, hum_cards)
                hum_cards, com_cards = res_two[1], res_two[2]
            counter += 1
        print("No more cards!\n")
        if com_cards > hum_cards:
            print("\nYOU LOST. Maybe next time ;)")
        elif com_cards < hum_cards:
            print("\nYOU WIN!!! Congrats!")
        else:
            print("\nIt's a tie. No one wins.")
        print(
            f"Final score:\nYou: {hum_cards} | Computer: {com_cards}"
        )
        highscores.highscores().long_scores(player, hum_cards, counter)

    def ask_input(self) -> None:
        if self.cheat:
            return True
        """Gets the input from unit (to continue drawing cards)."""
        arg = input("Would you like to continue ('enter' or 'yes')? ")
        if arg.upper() == "CHEAT":
            self.cheat = True
            return True
        return arg.upper() in ["Y", "YES", "TRUE", "1", ""]

    def print_screen(self, arg, human_cards, computer_cards) -> None:
        """Repetitive print function."""
        if arg:
            print(
                f"Great! You win!!!\nYou have {human_cards} cards"
                f" and the computer has {computer_cards}")
        else:
            print(
                f"The computer wins!!!\nYou have {human_cards} cards"
                f" and the computer has {computer_cards}"
            )

    def who_wins(self, com, hum, v_com, v_hum) -> tuple:
        """Decides who wins."""
        if v_com > v_hum:
            com += 1
            hum -= 1
        else:
            hum += 1
            com -= 1
        return (self.print_screen(v_hum > v_com, hum, com), hum, com)

    def war(self, com, hum) -> tuple:
        """In case of a draw."""
        print("\nSAME CARDS, WAR!")
        c = card.Card()
        hum_c, com_c = c.random_card(), c.random_card()
        val_h, val_c = c.value(hum_c), c.value(com_c)
        if val_h == val_c:
            return self.war(com, hum)
        elif val_h > val_c:
            hum += 4
            com -= 4
        else:
            com += 4
            hum -= 4
        print(f"You: {hum_c:<8} Computer: {com_c}")
        return (self.print_screen(val_h > val_c, hum, com), hum, com)
