# War Game Project

War Game project for the "Methods of Sustainable Programming" course, teached by Mikael Roos.<br />
Group members are: Einav Zilka, Dzenis Madzovic and Luan Rexhepi.

## Description
War (also known as Battle in the United Kingdom) is a simple card game, typically played by two players using a standard playing card deck — and often played by children. There are many variations, as well as related games such as the German 32-card Tod und Leben ("Life and Death").<br />
This is an implementation of the War card game, made completely in python. Our implementation of the war game includes two game modes:
* Short - played for 26 turns, winner is decided by who has more cards in their deck. Scores are based on the number of cards.
* Long - played until one of the players loses all cards. Scores are based on the number of draws it took to finish the game.

## Getting Started

### Dependencies

* Firstly, create a virtual enviroument by running "make venv".
```
$ make venv
```
* Activate the venv by running the commands given in the command line.
* To install all of the dependencies, run "make install"
```
$ make install
```

### Running The Game

* Make sure that all of the dependencies are install
* To run the game, go to the war directory and run main.py

### Executing program

* After the game is ecexuted from the war directory through main.py module, user is going to be promped to chose a player name.
* A new feature will appear in the screen asking the player to chose between four options, such as:
* Start - the short version of the game will be initiated (26 turns).
* Long - the long version of the game will be initiated (the game continues until one of the players loses all cards).
* Changename - option to allow user to change tha player name.
* Exit - exit the game.
* Help - additional help.
* Following the option choosen by the player (short or long) the game will be played by pressing enter key and the random cards are going to be drawn for the user and the computer. If it's a tie (same cards) a war option of the game will be initiated (war is not a feature in the short version).
* 

## Unit testing

* Activate the virtual environement 
* For Windows:
```
$ . .venv/Scripts/activate
```
* For Mac:
```
$ . .venv/bin/activate
```
* After the virtual environmental is activated then run the following command:
```
$ make test
```
* Make test will run all test files and make coverage test. Coverage results will be generated to a html report.


## Generating documentation

* Activate the virtual environement 
* For Windows:
```
$ . .venv/Scripts/activate
```
* For Mac:
```
$ . .venv/bin/activate
```
* After the virtual environmental is activated than run the following command:
```
$ make doc
```
* The "make doc" command will generate documentation and uml diagram. All the documentation files will be stored under new folder named "doc".
```
$ cd doc/
```
* Under uml/ directory you can find the uml diagram.
* Umder api/ directory you can find the comments and code documentation.

## Help

For help during the game, type following command line for additional information:
```
$ help
```

## Authors
* Einav Zilka
* Dzenis Madzovic
* Luan Rexhepi


## Version History


## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## References

* [Github Repo](https://github.com/PsychicPlatypus/WARGAME-project)
* [war-wiki](https://en.wikipedia.org/wiki/War_(card_game))


