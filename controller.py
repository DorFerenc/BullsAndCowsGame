import bh
import main_game_screen

class Controller:
    def __init__(self):
        self.bh = bh
        self.front = main_game_screen

    # def __client_asks_num_of_digits(self):
    #     #send: -
    #     #recv: num of digits
    #     return self.bh.NumberOfDigits
    #
    # def __client_asks_num_of_games(self):
    #     #send: -
    #     #recv: num of games
    #     return self.bh.NumberOfGames

    def __bh_asks_num_of_digits(self):
        #send: -
        #recv: num of digits
        self.bh.NumberOfDigits = self.front.getDigits()

    def __bh_asks_num_of_games(self):
        #send: -
        #recv: num of games
        self.bh.NumberOfGames = self.front.getGames()


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