from tkinter import *
from tkinter import ttk
from pathlib import Path
import tkinter as tk
from tkinter import Canvas, Entry, PhotoImage, Text, Button
from guess_functions import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def update_progress_bar(self, value):
    self.progress_bar["value"] = value
    self.canvas.update_idletasks()


class Bull_and_cows_stats_screen:
    def update_num_of_digits_value(self, event):
        self.number_of_digits_label.config(text=f"Number of digits {self.scale_num_of_digits.get()}")

    def update_num_of_games_value(self, event):
        self.number_of_games_label.config(text=f"Number of games {self.scale_num_of_games.get()}")

    def __init__(self, stats_screen):
        # define some constants
        self.OFFSET_MENU = 30

        # configure the root window
        stats_screen.geometry("1273x685")
        stats_screen.configure(bg="#F0F0F3")
        stats_screen.title("Bulls and Hits - Statistics")

        # create the canvas
        self.canvas = Canvas(
            stats_screen,
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
        self.scale_num_of_digits = Scale(self.canvas, variable=self.value_number_of_digits, from_=4, to=12, orient=HORIZONTAL, length=200)
        self.scale_num_of_digits.bind("<ButtonRelease-1>", self.update_num_of_digits_value)
        self.scale_num_of_digits.place(x=650, y=100)
        self.number_of_digits_label = ttk.Label(self.canvas, text=f"Number of digits {self.scale_num_of_digits.get()}", foreground="#7C0AA4", font=("Inter Regular", 15 * -1))
        self.number_of_digits_label.place(x=650, y=80)


        self.button_image_Guess = PhotoImage(file=relative_to_assets("button_Guess.png"))
        self.button_Guess = Button(image=self.button_image_Guess, borderwidth=0, highlightthickness=0,
                              command=lambda: take_the_guess(self.ENTRY_LIST, self.canvas, self.BULLS_HITS_LIST), relief="flat")
        self.button_Guess.place(x=470, y=175, width=250.0, height=70.1025390625)

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



    def __relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

if __name__ == '__main__':
    stats_screen = Tk()
    stats_screen.title("Bulls & Hits")
    stats_screen.geometry("1273x685")
    stats_screen.configure(bg="#F0F0F3")
    # game = Codebreaker(window_main_screen)
    stats_screen.resizable(False, False)
    Bull_and_cows_stats_screen(stats_screen)
    stats_screen.mainloop()
