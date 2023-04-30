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
from pathlib import Path
import tkinter as tk
from tkinter import ttk

from guess_functions import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def update_progress_bar(self, value):
    self.progress_bar["value"] = value
    self.canvas.update_idletasks()


class Bull_and_cows_stats_screen(ttk.Frame):

    def update_num_of_digits_value(self, event):
        self.number_of_digits_label.config(text=f"Number of digits {self.scale_num_of_digits.get()}")

    def update_num_of_games_value(self, event):
        self.number_of_games_label.config(text=f"Number of games {self.scale_num_of_games.get()}")

    def run_game(self):
      #  print(f"here {self.my_controller}, and {self.scale_num_of_games.get()}")
        self.my_view_controller.run_bh(self.scale_num_of_digits.get(), self.scale_num_of_games.get())

    def view_asks_for_graphs(self):
        self.my_view_controller.show_graphs()

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.my_view_controller = controller

    def __init__(self, parent):
        super().__init__(parent)
        # define some constants
        self.OFFSET_MENU = 30
        self.stats_screen = parent
        # self.my_controller = Controller

        # configure the root window
        self.stats_screen.geometry("1273x685")
        self.stats_screen.configure(bg="#F0F0F3")
        self.stats_screen.title("Bulls and Hits - Statistics")

        # create the canvas
        self.canvas = Canvas(
            self.stats_screen,
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

        # create the title text
        self.canvas.create_text(
            294.0,
            23.0,
            anchor="nw",
            text="Bulls and Hits - Statistics",
            fill="#745FF2",
            font=("Inter Regular", 48 * -1)
        )

        # number of games scale and label
        self.value_number_of_games = IntVar()
        self.scale_num_of_games = Scale(self.canvas, variable=self.value_number_of_games, from_=10, to=35, orient=HORIZONTAL, length=200)
        self.scale_num_of_games.bind("<ButtonRelease-1>", self.update_num_of_games_value)
        self.scale_num_of_games.place(x=300, y=100)
        self.number_of_games_label = ttk.Label(self.canvas, text=f"Number of digits {self.scale_num_of_games.get()}", foreground="#7C0AA4", font=("Inter Regular", 15 * -1))
        self.number_of_games_label.place(x=300, y=80)

        # number of digits scale and label
        self.value_number_of_digits = IntVar()
        self.scale_num_of_digits = Scale(self.canvas, variable=self.value_number_of_digits, from_=4, to=8, orient=HORIZONTAL, length=200)
        self.scale_num_of_digits.bind("<ButtonRelease-1>", self.update_num_of_digits_value)
        self.scale_num_of_digits.place(x=650, y=100)
        self.number_of_digits_label = ttk.Label(self.canvas, text=f"Number of games {self.scale_num_of_games.get()}", foreground="#7C0AA4", font=("Inter Regular", 15 * -1))
        self.number_of_digits_label.place(x=650, y=80)


        # self.button_image_Guess = PhotoImage(file=relative_to_assets("button_Guess.png"))
        # self.button_Guess = Button(image=self.button_image_Guess, borderwidth=0, highlightthickness=0,
        #                            command=self.run_game, relief="flat")
        # self.button_Guess.place(x=470, y=175, width=250.0, height=70.1025390625)
        self.run_game_button = Button(text='Run Game!', command=self.run_game)
        self.run_game_button.place(x=360, y=148)

        # self.button_image_Guess2 = PhotoImage(file=relative_to_assets("button_Guess.png"))
        # self.button_Guess2 = Button(image=self.button_image_Guess2, borderwidth=0, highlightthickness=0,
        #                            command=self.view_asks_for_graphs, relief="flat")
        # self.button_Guess2.place(x=570, y=220, width=250.0, height=70.1025390625)
        self.show_graphs_button = Button(text='Show Graphs!', command=self.view_asks_for_graphs)
        self.show_graphs_button.place(x=690, y=148)

        self.button_image_new_game = PhotoImage(file=relative_to_assets("button_new_game.png"))
        self. button_new_game = Button(image=self.button_image_new_game, borderwidth=0, highlightthickness=0,
                                 command=lambda: print("button_new_game clicked"), relief="flat")
        self.button_new_game.place(x=13.0, y=23.0 + self.OFFSET_MENU, width=250.0, height=70.1025390625)

        self.button_image_prev_game = PhotoImage(file=relative_to_assets("button_prev_game.png"))
        self.button_prev_game = Button(image=self.button_image_prev_game, borderwidth=0, highlightthickness=0,
                                  command=lambda: print("button_prev_game clicked"), relief="flat")
        self.button_prev_game.place(x=13.0, y=108.0 + self.OFFSET_MENU, width=250.0, height=70.1025390625)

        self.button_image_settings = PhotoImage(file=relative_to_assets("button_settings.png"))
        self.button_settings = Button(image=self.button_image_settings, borderwidth=0, highlightthickness=0,
                                 command=lambda: print("button_settings clicked"), relief="flat")
        self.button_settings.place(x=13.0, y=193.0 + self.OFFSET_MENU, width=250.0, height=70.1025390625)

        self.button_image_stats = PhotoImage(file=relative_to_assets("button_stats.png"))
        self.button_stats = Button(image=self.button_image_stats, borderwidth=0, highlightthickness=0,
                              command=lambda: print("button_stats clicked"), relief="flat")
        self.button_stats.place(x=14.0, y=278.0 + self.OFFSET_MENU, width=250.0, height=70.1025390625)

        self.create_graphs(None) # open an empty graph

    def create_graphs(self, fig):
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

    def create_graphs2(self, fig):
        # stats_screen = tk.Tk()
        # stats_screen.title("Scrollbar Widget Example")

        # # apply the grid layout
        # root.grid_columnconfigure(0, weight=1)
        # root.grid_rowconfigure(0, weight=1)

        # create the text widget
        text = tk.Text(self.canvas, height=40, width=60)
        text.grid(row=0, column=0, sticky=tk.EW)
        # text.place(x=100, y=100)

        # create a scrollbar widget and set its command to the text widget
        scrollbar = ttk.Scrollbar(self.canvas, orient='vertical', command=text.yview)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        #  communicate back to the scrollbar
        text['yscrollcommand'] = scrollbar.set

        # Create a canvas to embed the plot
        canvas = FigureCanvasTkAgg(fig, master=self.stats_screen)
        canvas.draw()

        # get the plot as a base64 encoded string
        buf = BytesIO()
        canvas.print_figure(buf, format='png')
        data = base64.b64encode(buf.getbuffer()).decode('ascii')

        # insert the plot into the text widget
        photo = tk.PhotoImage(data=data)
        text.image_create(tk.END, image=photo)


    def __relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

# if __name__ == '__main__':
#     stats_screen = Tk()
#     stats_screen.title("Bulls & Hits")
#     stats_screen.geometry("1273x685")
#     stats_screen.configure(bg="#F0F0F3")
#     # game = Codebreaker(window_main_screen)
#     stats_screen.resizable(False, False)
#     Bull_and_cows_stats_screen(stats_screen)
#     stats_screen.mainloop()
