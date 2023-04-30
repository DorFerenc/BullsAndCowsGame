import base64
import tkinter as tk
from io import BytesIO
from tkinter import ttk
import matplotlib.pyplot as plt
from PIL import ImageTk
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

# # create a Tkinter window
# root = tk.Tk()
# root.geometry("800x600")
#
# # create a text widget
# text = tk.Text(root)
# # text.pack(side="left", fill="y")
#
# # create a canvas widget
# canvas = tk.Canvas(text)
# # canvas.pack(fill="both", expand=True)
#
# # create a matplotlib figure
# fig, ax = plt.subplots()
# ax.plot([1, 2, 3], [4, 5, 6])
# ax.set_title("Example Plot")
#
# # add the figure to the canvas
# # canvas.draw()
# figure_x, figure_y, figure_w, figure_h = canvas.bbox("all")
# figure_w, figure_h = int(figure_w), int(figure_h)
# photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)
# canvas.create_image(0, 0, image=photo, anchor="nw")
# fig_canvas = FigureCanvasTkAgg(fig, master=photo)
# fig_canvas.draw()
# fig_photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)
# fig_photo.tk_photoimage = fig_photo  # prevent garbage collection
# fig_photo.blank()  # create transparent image
# canvas.create_image(0, 0, image=fig_photo, anchor="nw")
# canvas.create_window(0, 0, window=fig_canvas.get_tk_widget(), anchor="nw")
#
# # add labels and spaces between the graphs
# text.insert("end", "\n\nLabel 1\n\n")
# text.window_create("end", window=canvas)
#
# text.insert("end", "\n\nLabel 2\n\n")
#
# # add a scrollbar
# scrollbar = ttk.Scrollbar(root, orient="vertical", command=text.yview)
# scrollbar.pack(side="right", fill="y")
# text.configure(yscrollcommand=scrollbar.set)
#
# # start the Tkinter event loop
# root.mainloop()
from matplotlib.figure import Figure

import model_graphs
from model_graphs import Graph_Model

class Zoobi(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.zoobi_screen = parent
        self.zoobi_screen.geometry("1273x685")

        # create the canvas
        self.canvas = tk.Canvas(
            self.zoobi_screen,
            bg="#F0F0F3",
            height=685,
            width=1273,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.pack(fill=tk.BOTH, expand=1)

        # create the blue menu on the left
        self.canvas.create_rectangle(0.0, 0.0, 276.0, 685.0, fill="#3A7FF6", outline="")
        self.canvas.create_text(13.0, 8.0, anchor="nw", text="Menu:", fill="#FF738E", font=("Inter Regular", 32 * -1))

        # create the orange canvas on the right
        self.orange_canvas = self.canvas.create_rectangle(900.0, 0.0, 1273.0, 685.0, fill="#FFA53C", outline="")
        self.canvas.create_text(920.0, 8.0, anchor="nw", text="Graphs:", fill="#7e37ad",
                                font=("Inter Regular", 32 * -1))


    # def create_graphs3(self, fig):
    #     # create the inner canvas
    #     inner_canvas = tk.Canvas(self.canvas, width=600, height=350)
    #     inner_canvas.place(x=276, y=200)
    #
    #     # create FigureCanvasTkAgg object
    #     figure_canvas = FigureCanvasTkAgg(fig, inner_canvas)
    #     # figure_canvas.draw()
    #
    #     # create the toolbar
    #     NavigationToolbar2Tk(figure_canvas, inner_canvas)
    #
    #     # pack the figure_canvas into the inner canvas
    #     figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


    def create_graphs3(self, fig):
        # create the inner canvas
        inner_canvas = tk.Canvas(self.canvas)
        inner_canvas.place(x=276, y=200, width=620, height=480)

        # # create a vertical scrollbar for the inner canvas
        # scrollbar = tk.Scrollbar(self.canvas, orient=tk.VERTICAL, command=inner_canvas.yview)
        # scrollbar.place(x=876, y=100, height=500)
        # inner_canvas.configure(yscrollcommand=scrollbar.set)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(fig, inner_canvas)

        # # create the toolbar
        NavigationToolbar2Tk(figure_canvas, inner_canvas)

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # def create_graphs3(self, fig):
    #     # create the inner canvas
    #     inner_canvas = tk.Canvas(self.canvas)
    #     inner_canvas.grid(row=0, column=0, padx=276, pady=100, sticky=tk.NSEW)
    #
    #     # create a frame to hold the figure and scrollbar
    #     frame = tk.Frame(inner_canvas)
    #     frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    #
    #     # create a vertical scrollbar for the frame
    #     vsb = tk.Scrollbar(inner_canvas, orient="vertical", command=inner_canvas.yview)
    #     # vsb.grid(row=0, column=1, sticky=tk.NS)
    #     inner_canvas.configure(yscrollcommand=vsb.set)
    #
    #     # create FigureCanvasTkAgg object
    #     figure_canvas = FigureCanvasTkAgg(fig, frame)
    #     figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    #
    #     # create the toolbar
    #     NavigationToolbar2Tk(figure_canvas, frame)
    #
    #     # create a text widget for displaying graphs
    #     text_widget = tk.Text(frame, wrap=tk.NONE)
    #     text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    #
    #     # link the scrollbar to the text widget
    #     text_widget.config(yscrollcommand=vsb.set)
    #     vsb.config(command=text_widget.yview)
    #
    #     # add the figure to the text widget
    #     text_widget.window_create(tk.END, window=figure_canvas.get_tk_widget())

    # def create_graphs3(self, fig):
    #     # create the inner canvas
    #     inner_canvas = tk.Canvas(self.canvas)
    #     # inner_canvas.grid(row=0, column=0, sticky=tk.EW)
    #     inner_canvas.pack()
    #     # create FigureCanvasTkAgg object
    #     figure_canvas = FigureCanvasTkAgg(fig, inner_canvas)
    #
    #     # create the toolbar
    #     NavigationToolbar2Tk(figure_canvas, inner_canvas)
    #
    #     figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


    def create_graphs2(self, fig):
        # # Create the inner canvas inside the outer canvas
        # inner_canvas = tk.Canvas(self.canvas, width=300, height=300)
        # self.canvas.create_window(50, 50, window=inner_canvas)
        #
        # # create a canvas to display the image
        # # canvas = tk.Canvas(root, width=300, height=300)
        # # canvas.pack(side=tk.LEFT)
        #
        # # load the image and convert it to a Tkinter-compatible format
        # image = tk.Image.open("image.jpg")
        # tk_image = ImageTk.PhotoImage(image)
        #
        # # add the image to the canvas
        # inner_canvas.create_image(0, 0, anchor="nw", image=tk_image)
        #
        # # create a scrollbar and link it to the canvas
        # scrollbar = tk.Scrollbar(inner_canvas, orient=tk.VERTICAL, command=inner_canvas.yview)
        # scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # inner_canvas.configure(yscrollcommand=scrollbar.set)
        #
        # # make the canvas scrollable
        # inner_canvas.configure(scrollregion=inner_canvas.bbox("all"))

        # create the inner canvas
        inner_canvas = tk.Canvas(self.canvas)
        inner_canvas.grid(row=0, column=0, sticky=tk.EW)
        # inner_canvas.pack()

        # add the figure to the inner canvas
        graph_canvas = FigureCanvasTkAgg(fig, master=inner_canvas)
        canvas_widget = graph_canvas.get_tk_widget()
        canvas_widget.pack()
        # canvas_widget.place(x=80, y=20)
        # add scrollbar to inner_canvas
        yscrollbar = tk.Scrollbar(inner_canvas, orient="vertical", command=inner_canvas.yview)
        yscrollbar.pack(side="right", fill="y")
        inner_canvas.configure(yscrollcommand=yscrollbar.set)


        # # # create a scrollbar widget and set its command to the text widget
        # scrollbar = ttk.Scrollbar(inner_canvas, orient='vertical', command=inner_canvas.yview)
        # scrollbar.pack(side="right", fill="y")
        # #
        # # #  communicate back to the scrollbar
        # inner_canvas['yscrollcommand'] = scrollbar.set



        # configure inner_canvas to contain the figure
        inner_canvas.configure(scrollregion=inner_canvas.bbox("all"))
        # inner_canvas.place(x=276, y=300)

        # add the inner canvas to the outer canvas
        self.canvas.create_window(276, 300, anchor="nw", window=inner_canvas)

        pass

    def create_graphs(self, fig):
        # stats_screen = tk.Tk()
        # stats_screen.title("Scrollbar Widget Example")
        #
        # # create a Tkinter window
        # root = tk.Tk()
        # root.geometry("800x600")
        #
        # # apply the grid layout
        # root.grid_columnconfigure(0, weight=1)
        # root.grid_rowconfigure(0, weight=1)
        graph_frame = ttk.Frame(self.canvas, width=350, height=70)
        graph_frame.place(x=276, y=300)
        # create the text widget
        text = tk.Text(graph_frame, height=23, width=75)
        text.grid(row=0, column=0, sticky=tk.EW)
        # text.place(x=276, y=300)
        #
        # # create a scrollbar widget and set its command to the text widget
        scrollbar = ttk.Scrollbar(graph_frame, orient='vertical', command=text.yview)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)
        #
        # #  communicate back to the scrollbar
        text['yscrollcommand'] = scrollbar.set
        #
        # Create a canvas to embed the plot
        canvas = FigureCanvasTkAgg(fig)
        canvas.draw()
        #
        # # get the plot as a base64 encoded string
        buf = BytesIO()
        canvas.print_figure(buf, format='png')
        data = base64.b64encode(buf.getbuffer()).decode('ascii')

        # insert the plot into the text widget
        photo = tk.PhotoImage(data=data)
        text.image_create(tk.END, image=photo)
        #
        # root.mainloop()



def get_fig():
    # initialize empty lists for game number and number of tries
    game_numbers = []
    num_tries = []

    # initialize empty lists for table sizes and guess numbers
    table_sizes = []
    guess_numbers = []

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
                game_numbers.append(int(game_number.group(1)))
                num_tries.append(int(tries.group(1)))

            guess_numbers_list = game_data.split("guess")
            for guess in guess_numbers_list:
                # table_size = (re.search(r'table size:\s+(\d+)', game_data)) # .group(1))
                guess_number = (re.search(r'number\s+(\d+)\s+is:', guess))  # .group(1))
                table_size = (re.search(r'number\s+\d+\s+is:\s+\d+\s+table size:\s+(\d+)', guess))  # .group(1))

                # check if both regex searches were successful
                if table_size and guess_number:
                    table_sizes.append(int(table_size.group(1)))
                    guess_numbers.append(int(guess_number.group(1)))

    # create a Figure object and two subplots

    fig = plt.Figure(figsize=(6, 6), dpi=100)
    fig.subplots_adjust(hspace=0.5)
    # axes = fig.add_subplot()
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    # create the first plot
    ax1.bar(game_numbers, num_tries)
    ax1.set_xlabel("Game Number")
    ax1.set_ylabel("Number of Tries")
    ax1.set_title("Number of Tries vs Game Number")

    # create the second plot
    ax2.scatter(guess_numbers, table_sizes, alpha=0.5)
    ax2.set_xlabel("Guess Number")
    ax2.set_ylabel("Table Size")
    ax2.set_title("Table Size vs Guess Number")

    # convert the figure to an image
    # fig.canvas.draw()
    # img = tk.Image.frombytes('RGB', fig.canvas.get_width_height(), fig.canvas.tostring_rgb())
    # convert the image to a Tkinter PhotoImage
    # photo = ImageTk.PhotoImage(img)
    # # create the canvas and add the image to it
    # root = tk.Tk()
    # canvas = tk.Canvas(root, width=img.width, height=img.height)
    # canvas.create_image(0, 0, anchor='nw', image=photo)
    # canvas.pack()
    # return photo
    return fig


def get_fig_canvas(dady):
    # initialize empty lists for game number and number of tries
    game_numbers = []
    num_tries = []

    # initialize empty lists for table sizes and guess numbers
    table_sizes = []
    guess_numbers = []
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
                game_numbers.append(int(game_number.group(1)))
                num_tries.append(int(tries.group(1)))

            guess_numbers_list = game_data.split("guess")
            for guess in guess_numbers_list:
                # table_size = (re.search(r'table size:\s+(\d+)', game_data)) # .group(1))
                guess_number = (re.search(r'number\s+(\d+)\s+is:', guess))  # .group(1))
                table_size = (re.search(r'number\s+\d+\s+is:\s+\d+\s+table size:\s+(\d+)', guess))  # .group(1))

                # check if both regex searches were successful
                if table_size and guess_number:
                    table_sizes.append(int(table_size.group(1)))
                    guess_numbers.append(int(guess_number.group(1)))

    # self.title('Tkinter Matplotlib Demo')

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
    figure_canvas = FigureCanvasTkAgg(figure, dady)

    # create the toolbar
    NavigationToolbar2Tk(figure_canvas, dady)

    # create axes
    axes = figure.add_subplot()

    # create the barchart
    axes.bar(game_numbers, num_tries)
    axes.set_title('Top 5 Programming Languages')
    axes.set_ylabel('Popularity')

    figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo')
        view1_screen_stats = Zoobi(self)

        figy = get_fig()
        view1_screen_stats.create_graphs3(figy)

if __name__ == '__main__':
    app = App()
    app.mainloop()