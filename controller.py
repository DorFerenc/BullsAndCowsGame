import os

import bh
import sys

import stats_screen


class Controller():
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.table_size = len(self.model.getCounter(self.view))
        self.guess = None
        # self.bh_code = bh
        # self.my_stats_screen = stats_screen.Bull_and_cows_stats_screen()

    def run_bh(self, num_of_digits, num_of_games):
        """
        :param num_of_digits:
        :param num_of_games:
        :return: -
        this function initiate bh
        """
        self.guess = self.view.take_the_guess(self.view)
        self.l = []
        for i in range(num_of_games):
            game_num = str(i+1)
            self.view.update_current_guess_board(self.view)
            current_round = bh.BH(0, numberOfDigits=num_of_digits)
            self.l.append(current_round.getCounter())
            current_round_size = current_round.getCounter()
            avg = str(sum(self.l) / len(self.l))
            self.view.show_game(self.view, game_num, self.guess, current_round_size)



    def bh_asks_the_guess(self):
        """
        #send: -
        #recv: str
        :return:
        """
        self.model.get_guess(self.model, self.view.take_the_guess())

    def client_request_for_NH(self):
        #send: -
        #recv: num of hits
        pass

    def client_request_for_NB(self):
        #send: -
        #recv: num of bulls
        pass


    def client_asks_if_its_a_win(self):
        #send: guess
        #recv: boolean
        pass

    def client_request_table_size(self):
        #send: -
        #recv: int or str
        pass

    def client_request_num_of_tries(self):
        #send: -
        #recv: int
        pass

