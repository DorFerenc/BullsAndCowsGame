import os
import bh
from bh import BH
import sys

import stats_screen
from main_game_screen import Bull_and_cows_main_screen
from stats_screen import Bull_and_cows_stats_screen


class Controller():
    def __init__(self, model_play_game, model_graph, model_bh_orig, container):
        self.model_play_game = model_play_game
        self.model_graph = model_graph
        self.model_bh_orig = model_bh_orig
        self.container = container

        self.frames = {} # initializing frames to an empty array

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
        # self.bh_code = bh
        # self.my_stats_screen = stats_screen.Bull_and_cows_stats_screen()

    # to display the current frame passed as
    # parameter
    def show_frame(self, view_num):
        cont = Bull_and_cows_main_screen
        if view_num == 2:
            cont = Bull_and_cows_stats_screen
            self.view1_screen_stats.create_graphs(None)
            self.view1_screen_stats.show_text("")
        frame = self.frames[cont]
        frame.tkraise()

    def run_bh(self, num_of_digits, num_of_games):
        """
        :param num_of_digits:
        :param num_of_games:
        :return: -
        this function initiate bh
        """
        self.guess = self.view2_main_screen.take_the_guess(self.view2_main_screen)
        self.l = []
        for i in range(num_of_games):
            game_num = str(i + 1)
            self.view2_main_screen.update_current_guess_board(self.view2_main_screen)
            current_round = bh.BH(0, numberOfDigits=num_of_digits)
            self.l.append(current_round.getCounter())
            current_round_size = current_round.getCounter()
            avg = str(sum(self.l) / len(self.l))
            self.view2_main_screen.show_game(self.view2_main_screen, game_num, self.guess, current_round_size)

    def run_stats(self, num_of_digits, num_of_games):
        """
        :param num_of_digits:
        :param num_of_games:
        :return: -
        this function initiate bh
        """
        self.view1_screen_stats.create_graphs(None)
        self.view1_screen_stats.show_text("")
        sys.stdout = open("bhOutput.txt", 'w')
        l = []
        for i in range(num_of_games):
            print("\ngame number ", str(i + 1))
            current_round = bh.BH(0, numberOfDigits=num_of_digits)
            l.append(current_round.getCounter())
        print("average number of guesses for ", \
              str(num_of_games), " games is: ", \
              sum(l) / len(l))
        sys.stdout.close()
        # while True:
        #     f_stat = os.stat("bhOutput.txt")
        #     if not bool(f_stat.st_mode & 0o100000):  # check if file is closed
        #         break

    def bh_asks_the_guess(self):
        """
        #send: -
        #recv: str
        :return:
        """
        self.model_play_game.get_guess(self.model_play_game, self.view2_main_screen.take_the_guess())

    def set_table_size(self):
        """
        #send: -
        #recv: str
        :return:
        """
        self.table_size = len(BH.getCounter(BH))

    def show_graphs(self):
        figy = self.model_graph.get_fig()
        texty = self.model_graph.get_text()
        self.view1_screen_stats.create_graphs(figy)
        self.view1_screen_stats.show_text(texty)

    def client_request_for_NH(self):
        # send: -
        # recv: num of hits
        pass

    def client_request_for_NB(self):
        # send: -
        # recv: num of bulls
        pass

    def client_asks_if_its_a_win(self):
        # send: guess
        # recv: boolean
        pass

    def client_request_table_size(self):
        # send: -
        # recv: int or str
        pass

    def client_request_num_of_tries(self):
        # send: -
        # recv: int
        pass
