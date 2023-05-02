# Bull and Cows Game
* This is a Python implementation of the Bull and Cows game, both for playing 
locally and gaining knowledge of usage by generating the computer to run the game 
and getting the results as graphs and raw data.

* This implementation includes a graphical user interface (GUI) using the tkinter library. 

## Requirements
* Python 3.6 or higher
* tkinter library 

## How to run the game
* To run the game, execute the following command in the terminal: **python main.py**
* You can also right-click on the **main.py** file and and click on **Run 'main'**

## How to play the game
New game → single local player mode:
1. Screen will load on New Game
2. Enter your guess entry fields using the number keys on the screen
3. Click the "Guess" button to check your guess.
4. The program will display the number of bulls and cows for each guess.
5. Keep guessing until you either guess the secret number or run out of guesses.
6. If you guess the secret number within the allowed number of guesses, you win the game! Otherwise, you lose.

Stats → computer generates data mode
1. Switch screen to Stats
2. Give your desired specifications to the computer (both number of games and number of digits) 
3. Click the "Run Game!" button generate the data.
4. Click the "Show Graphs!" button to see the graphs and the data.
5. Keep changing your specifications until you acquire your desired knowledge.

## File structure
* 'main.py': The main file that runs the game.
* 'bh.py': The file that contains the game logic for the stats part.
* 'main_game_screen.py': The file that contains the GUI for the local game.
* 'stats_screen.py': The file that contains the GUI for the statistics screen.
* 'bh_back.py' : The file that contains the model for the local game logic.
* 'model_graph.py': The file that contains the model for the graph generation logic.
* 'controller.py': The file that contains the controller logic for the GUI.
* 'assets': a folder with images for the GUI
* 'bhOutput.txt': a file holding the data
* README.md: This file.