import tkinter as tk
import re

import matplotlib

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # initialize empty lists for game number and number of tries
        self.game_numbers = []
        self.num_tries = []

        # initialize empty lists for table sizes and guess numbers
        self.table_sizes = []
        self.guess_numbers = []
        # open and read the text file
        with open("bhOutput.txt", "r") as file:
            # read the entire file contents as a string
            contents = file.read()
            # split the string into a list of game data sections
            game_data_list = contents.split(
                "=========================================================================== \n")

            # loop through each game data section
            for game_data in game_data_list:
                # search for the game number and number of tries using regex
                game_number = re.search(r"game number\s+(\d+)", game_data)
                tries = re.search(r"number of tries:\s+(\d+)", game_data)

                # check if both regex searches were successful
                if game_number and tries:
                    # append the game number and number of tries to the respective lists
                    self.game_numbers.append(int(game_number.group(1)))
                    self.num_tries.append(int(tries.group(1)))

                guess_numbers_list = game_data.split("guess")
                for guess in guess_numbers_list:
                    # table_size = (re.search(r'table size:\s+(\d+)', game_data)) # .group(1))
                    guess_number = (re.search(r'number\s+(\d+)\s+is:', guess))  # .group(1))
                    table_size = (re.search(r'number\s+\d+\s+is:\s+\d+\s+table size:\s+(\d+)', guess))  # .group(1))

                    # check if both regex searches were successful
                    if table_size and guess_number:
                        self.table_sizes.append(int(table_size.group(1)))
                        self.guess_numbers.append(int(guess_number.group(1)))

        self.title('Tkinter Matplotlib Demo')

        # prepare data
        data = {
            'Python': 11.27,
            'C': 11.16,
            'Java': 10.46,
            'C++': 7.5,
            'C#': 5.26
        }
        languages = data.keys()
        popularity = data.values()

        # create a figure
        figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, self)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(self.game_numbers, self.num_tries)
        axes.set_title('Top 5 Programming Languages')
        axes.set_ylabel('Popularity')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


if __name__ == '__main__':
    app = App()
    app.mainloop()