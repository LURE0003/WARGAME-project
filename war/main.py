"""
WAR GAME

"""

from war import shell

if __name__ == "__main__":
    print(__doc__)
    name = input("Choose a player name --> ")
    shell.Shell(name).cmdloop()
