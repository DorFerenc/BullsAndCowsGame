import bh
import sys

import stats_screen


class Controller():
    def __init__(self, model, view):
        self.model = model
        self.view = view
        # self.bh_code = bh
        # self.my_stats_screen = stats_screen.Bull_and_cows_stats_screen()

    def run_bh(self, num_of_digits, num_of_games):
        """
        :param num_of_digits:
        :param num_of_games:
        :return: -
        this function initiate bh
        """
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

    def bh_asks_the_guess(self):
        #send: -
        #recv: int or str
        pass
