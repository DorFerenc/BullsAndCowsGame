import re

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Graph_Model:
    def __init__(self):
        # initialize empty lists for game number and number of tries
        self.game_numbers = []
        self.num_tries = []

        # initialize empty lists for table sizes and guess numbers
        self.table_sizes = []
        self.guess_numbers = []

    def get_text(self):
        with open("bhOutput.txt", "r") as file:
            # read the entire file contents as a string
            contents = file.read()
        return contents

    def get_fig(self):
        # open and read the text file
        with open("bhOutput.txt", "r") as file:
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
                    # table_size = (re.search(r'table size:\s+(\d+)', game_data)) # .group(1))
                    guess_number = (re.search(r'number\s+(\d+)\s+is:', guess))  # .group(1))
                    table_size = (re.search(r'number\s+\d+\s+is:\s+\d+\s+table size:\s+(\d+)', guess))  # .group(1))

                    # check if both regex searches were successful
                    if table_size and guess_number:
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

        # for number in self.table_sizes:
        #     print(number)
        # create the second plot
        ax2.scatter(self.guess_numbers, self.table_sizes, alpha=0.5)
        ax2.set_xlabel("Guess Number")
        ax2.set_ylabel("Table Size")
        ax2.set_title("Table Size vs Guess Number")

        return fig
#
#
# root = tk.Tk()
# root.title("Scrollbar Widget Example")
#
# # apply the grid layout
# root.grid_columnconfigure(0, weight=1)
# root.grid_rowconfigure(0, weight=1)
#
# # create the text widget
# text = tk.Text(root, height=40, width=60)
# text.grid(row=0, column=0, sticky=tk.EW)
# # text.place(x=100, y=100)
#
# # create a scrollbar widget and set its command to the text widget
# scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
# scrollbar.grid(row=0, column=1, sticky=tk.NS)
#
# #  communicate back to the scrollbar
# text['yscrollcommand'] = scrollbar.set
#
#
# # Create a canvas to embed the plot
# canvas = FigureCanvasTkAgg(fig, master=root)
# canvas.draw()
#
# # get the plot as a base64 encoded string
# buf = BytesIO()
# canvas.print_figure(buf, format='png')
# data = base64.b64encode(buf.getbuffer()).decode('ascii')
#
# # insert the plot into the text widget
# photo = tk.PhotoImage(data=data)
# text.image_create(tk.END, image=photo)

# root.mainloop()
