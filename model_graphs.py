import re

import matplotlib.pyplot as plt


class Graph_Model:
    def __init__(self):
        """
        Initializes empty lists for game number and number of tries,
        and table sizes and guess numbers.
        """
        # initialize empty lists for game number and number of tries
        self.game_numbers = []
        self.num_tries = []

        # initialize empty lists for table sizes and guess numbers
        self.table_sizes = []
        self.guess_numbers = []

    def update_file(self, filename, num_digits):
        """
        Updates the formatting of guess results in the specified file.
        :param filename: the name of the file to update
        :type filename: str
        :param num_digits: number of digits in the current game
        :type num_digits: Int
        """
        # open the file in read mode and read the lines
        with open(filename, 'r') as file:
            lines = file.readlines()

        # iterate through the lines and update the formatting
        for i in range(len(lines)):
            if 'game number' in lines[i]:
                parts = lines[i].split()
                parts[2] = parts[2] + ","
                parts.append(f"number of digits {num_digits}")
                lines[i] = ' '.join(parts) + '\n'
            if 'guess number' in lines[i]:
                parts = lines[i].split()
                parts[2] = parts[2].ljust(2)
                parts[5] = parts[5].ljust(5)
                parts[7] = parts[7].ljust(9)
                parts[9] = parts[9].ljust(4)
                lines[i] = ' '.join(parts) + '\n'

        # open the file in write mode and write the updated lines
        with open(filename, 'w') as file:
            file.writelines(lines)

    def get_text(self, filename, num_digits):
        """
        Reads the contents of a file after updating the formatting of guess results.

        :param filename: the name of the file to read
        :type filename: str
        :param num_digits: number of digits in the current game
        :type num_digits: Int
        :return: the contents of the file after updating the formatting
        :rtype: str
        """
        self.update_file(filename, num_digits)
        with open(filename, "r") as file:
            # read the entire file contents as a string
            contents = file.read()
        return contents

    def get_fig(self, filename):
        """
        Generates two subplots showing the number of tries vs game number,
        and the table size vs guess number,
        using data extracted from the specified file.

        :param filename: the name of the file containing the game data
        :type filename: str
        :return: a matplotlib Figure object containing the two subplots
        :rtype: matplotlib.figure.Figure
        """
        # open and read the text file
        with open(filename, "r") as file:
            # read the entire file contents as a string
            contents = file.read()
            # split the string into a list of game data sections
            game_data_list = contents.split("=========================================================================== \n")

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
                    guess_number = (re.search(r'number\s+(\d+)\s+is:', guess))  # .group(1))
                    table_size = (re.search(r'number\s+\d+\s+is:\s+\d+\s+table size:\s+(\d+)', guess))  # .group(1))

                    # check if both regex searches were successful
                    if table_size and guess_number and (int(guess_number.group(1))) != 1:
                        self.table_sizes.append(int(table_size.group(1)))
                        self.guess_numbers.append(int(guess_number.group(1)))

        # create a Figure object and two subplots
        fig = plt.Figure(figsize=(6, 6), dpi=100)
        fig.subplots_adjust(hspace=0.5)
        fig.subplots_adjust(left=0.16, right=0.95)
        ax1 = fig.add_subplot(211)
        ax2 = fig.add_subplot(212)

        # create the first plot
        ax1.bar(self.game_numbers, self.num_tries)
        ax1.set_xlabel("Game Number")
        ax1.set_ylabel("Number of Tries")
        ax1.set_title("Number of Tries vs Game Number")

        # create the second plot
        ax2.scatter(self.guess_numbers, self.table_sizes, alpha=0.5)
        ax2.set_xlabel("Guess Number")
        ax2.set_ylabel("Table Size")
        ax2.set_title("Table Size vs Guess Number")

        return fig