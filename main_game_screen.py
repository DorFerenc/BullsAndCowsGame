from pathlib import Path
import tkinter as tk
from tkinter import Canvas, Entry, PhotoImage, Text, Button
from guess_functions import *


class Bull_and_cows_main_screen:
    def __init__(self, window_main_screen):
        # define some constants
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path("assets/frame0")
        self.OFFSET_MENU = 30

        # configure the root window
        window_main_screen.geometry("1273x685")
        window_main_screen.configure(bg="#F0F0F3")
        window_main_screen.title("Bulls and Hits")

        # create the canvas
        self.canvas = Canvas(
            window_main_screen,
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
        self.canvas.create_text(920.0, 8.0, anchor="nw", text="Guesses:", fill="#7e37ad",
                                font=("Inter Regular", 32 * -1))

        # create the title text
        self.canvas.create_text(
            294.0,
            23.0,
            anchor="nw",
            text="Bulls and Hits",
            fill="#745FF2",
            font=("Inter Regular", 48 * -1)
        )

        # create the entry widgets for guesses TextBoxes TODO DF add disabled function for the guesses
        entry_image_guess_1 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_guess_1 = self.canvas.create_image(330.0, 143.05126953125, image=entry_image_guess_1)
        self.entry_guess_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font='Georgia 20')
        self.entry_guess_1.place(x=294.0, y=108.0, width=72.0, height=68.1025390625)

        entry_image_guess_2 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_guess_2 = self.canvas.create_image(419.5, 143.05126953125, image=entry_image_guess_2)
        self.entry_guess_2 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font='Georgia 20')
        self.entry_guess_2.place(x=384.0, y=108.0, width=71.0, height=68.1025390625)

        entry_image_guess_3 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_guess_3 = self.canvas.create_image(508.5, 143.05126953125, image=entry_image_guess_3)
        self.entry_guess_3 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font='Georgia 20')
        self.entry_guess_3.place(x=473.0, y=108.0, width=71.0, height=68.1025390625)

        entry_image_guess_4 = PhotoImage(file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_guess_4 = self.canvas.create_image(601.0, 143.05126953125, image=entry_image_guess_4)
        self.entry_guess_4 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font='Georgia 20')
        self.entry_guess_4.place(x=565.0, y=108.0, width=72.0, height=68.1025390625)

        # List of the guesses TextBoxes
        self.ENTRY_LIST = [self.entry_guess_1, self.entry_guess_2, self.entry_guess_3, self.entry_guess_4]

        # Text labels: Bulls, Hits
        self.canvas.create_text(310.0, 271.0, anchor="nw", text="Hits:", fill="#FF738E",
                                font=("Inter Regular", 32 * -1))
        self.entry_hits = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font='Georgia 13')
        self.entry_hits.place(x=405.0, y=273.0, width=30.0, height=30.0)

        self.canvas.create_text(310.0, 209.0, anchor="nw", text="Bulls:", fill="#FF738E",
                                font=("Inter Regular", 32 * -1))
        self.entry_bulls = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font='Georgia 13')
        self.entry_bulls.place(x=405.0, y=211.0, width=30.0, height=30.0)

        self.BULLS_HITS_LIST = [self.entry_bulls, self.entry_hits]  # List of the Text labels: Bulls, Hits

        self.canvas.create_text(
            607.0,
            220.0,
            anchor="nw",
            text="matching digits in the right positions",
            fill="#7B0AA3",
            font=("Inter Regular", 15 * -1)
        )

        self.canvas.create_text(
            607.0,
            282.0,
            anchor="nw",
            text="matching digits in different positions",
            fill="#7C0AA4",
            font=("Inter Regular", 15 * -1)
        )


if __name__ == '__main__':
    window_main_screen = Tk()
    window_main_screen.title("Bulls & Hits")
    window_main_screen.geometry("1273x685")
    window_main_screen.configure(bg="#F0F0F3")
    # game = Codebreaker(window_main_screen)
    window_main_screen.mainloop()
