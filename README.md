# hanafuda-koi-koi. 
### A simulation of the Koi Koi card game in Python, using multiple files to enact separation of concerns.

## What is Hanafuda?
Hanafuda are Japanese playing cards which literally translate to 'Flower Cards' in English. The deck is made of 48 cards, split into 12 suits with 4 members each. Each suit represents a month of the year. The cards typically depict different varieties of botany which showcase the seasonal flora of Japan over a year. 

This project simulates a hanafuda deck by defining cards using Class and inheritance to define each card as a unique object. The aim of this project is to provide a flexible deck which can be used as a base to apply towards playing Koi Koi. It is the hope that this project can be easily adapted to simulate other games using the hanafuda deck, such as the Korean game Go-Stop and the Hawaiian game Sakura.

## Koi Koi
This project supplies a Koi Koi simulator which applies the following rules:  

**Game Structure**
* 2 players take turns matching cards from their hands with cards belonging to the same month on the table.
* The aim is to make special sets, known as Yaku, using cards across the different months score points.
* As soon as a set is made by either person, the winning player can end the round or call Koi Koi to try and earn more points.
* If the round continues, it will end when another set is made by either player, or an existing set is added to / upgraded.
* When the round ends, points are only awarded to the last player who earned a set. 
* Games are made of either 3, 6, 9, or 12 rounds.
* The first player of round 1 is randomly chosen.
* The winning player of the last round begins plays first in the subsequent round.
* If the points scored in a single round are greater than or equal to 7 points, double the player score for that round.
* The player with the most points at the end of all rounds.

**Hanafuda Deck**
* 48 total cards made of:
  * 5 Light cards       - 1 Rainy Light, 1 Moon Light, 1 Cherry Blossom Light
  * 9 Seeds cards       - 3 Animals: 1 Boar, 1 Deer, 1 Butterfly
  * 10 Poetry cards     - 3 Blue, 3 Red
  * 24 Chaff cards      - 1 Sake Cup

**Sake Cup Card**
* The Sake Cup card counts as a Chaff and a Seeds card simultaneously. 
* Having this card enabled the two card special Viewing sets with either the Moon and Cherry Blossom Lights.

**Yaku (Scoring Sets)**
* 10 Chaff              = 1 point (+1 per)
* 5 Poetry              = 1 point (+1 per)
* 5 Seeds               = 1 point (+1 per)
* 3 Blue Poetry         = 5 points (+1 per poetry)
* 3 Red Poetry          = 5 points (+1 per poetry)
* 3 Boar-Deer-Butterfly = 5 points (+1 per seeds) - called the 'Animals' set in this simulator
* 2 Moon Viewing        = 5 points
* 2 Cherry Viewing      = 5 points
* 3 Three Lights        = 6 points
* 4 Rainy Four Lights   = 7 points
* 4 Four Lights         = 8 points
* 5 Five Lights         = 10 points

**Lucky Hands**
* 4 (all) of a month    = 6 points + instant win - 4 of a kind
* 4 pairs of 4 months   = 6 points + instant win - 4 pairs

## How to Run
To run Koi Koi locally, open the terminal and run the following command:
````console
python3 play.py
````

This will prompt you to input the names for Players 1 and 2, then it will ask how many rounds of Koi Koi you would like to play. It will then simulate a game, printing the scores and table for both players, and the hand of only the current active player. The user will input numbers to interact with the game and choices in the terminal.

## Future Work
Currently, Koi Koi can only be played locally by passing the same device between players. Future work would see this project implementing networking to enable players across devices to play together, or it would implement a bot player for individual users to play against. Further scope includes general improvements on the game GUI. Designing a tutorial to teach users how to play Koi Koi would also make this project more accessible.

## Notes
This project provides a yaku.txt to define the set names used in the game. Different games have used different names for these sets, for example, Light cards are also called Bright cards. By keeping the number of items and the order the same, this text file is provided as one which a user may manually customize to use their preferred names for the sets.

This project was built using Python 3.9.6.