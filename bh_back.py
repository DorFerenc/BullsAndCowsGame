from bh import BH

class BH_back:
    def __init__(self):
        # initialize empty lists for game number and number of tries
        self.game_numbers = ""
        self.num_tries = ""

        # initialize empty lists for table sizes and guess numbers
        self.table_sizes = ""
        self.guess_numbers = ""

        # initialize empty lists for num of bulls and num of hits
        self.nb = ""
        self.nh = ""

    def get_guess(self, guess):
        self.guess_numbers = guess

    def get_table_size(self):
        self.table_sizes = len(BH.getCounter(BH))