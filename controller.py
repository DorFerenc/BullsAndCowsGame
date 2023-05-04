import sys

import bh
from bh import BH
from main_game_screen import Bull_and_cows_main_screen
from stats_screen import Bull_and_cows_stats_screen


class Controller():
    def __init__(self, model_play_game, model_graph, container):
        """
        Initializes an instance of the Controller class.

        :param model_play_game: an instance of the BH_back class
        :type model_play_game: BH_back
        :param model_graph: an instance of the Graph_Model class
        :type model_graph: Graph_Model
        :param container: a container for holding the different frames of the application
        :type container: tkinter.Tk
        :return: None
        :rtype: None
        """
        self.model_play_game = model_play_game
        self.model_graph = model_graph
        self.container = container
        self.filename = "bhOutput.txt"
        self.frames = {}  # initializing frames to an empty array

        # iterating through a tuple consisting of the different page layouts
        for F in (Bull_and_cows_main_screen, Bull_and_cows_stats_screen):
            self.frame = F(self.container)
            self.frame.set_controller(self)
            self.frames[F] = self.frame
            self.frame.grid(row=0, column=0, sticky="nsew")

        self.view2_main_screen = self.frames[Bull_and_cows_main_screen]
        self.view1_screen_stats = self.frames[Bull_and_cows_stats_screen]

        self.show_frame(Bull_and_cows_main_screen)

        self.table_size = None
        self.guess = None

    # to display the current frame passed as parameter
    def show_frame(self, view_num):
        """
        Displays the frame with the given view number.

        :param view_num: the number of the frame to be displayed
        :type view_num: int
        :return: None
        :rtype: None
        """
        cont = Bull_and_cows_main_screen
        if view_num == 2:
            cont = Bull_and_cows_stats_screen
            self.view1_screen_stats.create_graphs(None)
            self.view1_screen_stats.show_text("")
        else:
            self.view2_main_screen.clear_all()
        frame = self.frames[cont]
        frame.tkraise()

    def main_view_asks_to_start_game(self, tries):
        """
        Initiates a new game with the specified number of tries.

        :param tries: the number of tries allowed in the game
        :type tries: int
        :return: None
        :rtype: None
        """
        self.model_play_game.initiate_game(tries)

    def main_sends_guess(self, guess):
        """
        Checks the given guess against the game solution
        and shows the results on the main screen.

        :param guess: the guess to be checked
        :type guess: str
        :return: None
        :rtype: None
        """
        res = self.model_play_game.check_guess(guess)
        self.view2_main_screen.show_what_returned_from_guess(res)

    def run_stats(self, num_of_digits, num_of_games):
        """
        Runs the game for the specified number of digits and games,
        and outputs the results to a file.

        :param num_of_digits: the number of digits to use in the game
        :type num_of_digits: int
        :param num_of_games: the number of games to run
        :type num_of_games: int
        :return: None
        :rtype: None
        """
        self.view1_screen_stats.create_graphs(None)
        self.view1_screen_stats.show_text("")
        sys.stdout = open("bhOutput.txt", 'w')
        l = []
        for i in range(num_of_games):
            print("\ngame number ", str(i + 1))
            current_round = bh.BH(0, numberOfDigits=num_of_digits)
            l.append(current_round.getCounter())
        print(f"""average number of guesses 
        for  : {str(num_of_games)} games, 
        with : {num_of_digits} digits,
        is   : {sum(l) / len(l)}""")
        sys.stdout.close()

    def bh_asks_the_guess(self):
        """
        Sends the current guess to the game model.

        :return: None
        :rtype: None
        """
        self.model_play_game.get_guess(self.model_play_game, self.view2_main_screen.take_the_guess())

    def set_table_size(self):
        """
        Sets the size of the game table.

        :return: None
        :rtype: None
        """
        self.table_size = len(BH.getCounter(BH))

    def show_graphs(self, num_digits):
        """
        Shows the graphs on the stats screen.

        :param num_digits: number of digits in the current game
        :type num_digits: Int
        :return: None
        :rtype: None
        """
        figy = self.model_graph.get_fig(self.filename)
        texty = self.model_graph.get_text(self.filename, num_digits)
        self.view1_screen_stats.create_graphs(figy)
        self.view1_screen_stats.show_text(texty)
