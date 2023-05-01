import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Entry, PhotoImage, Button

NumberOfDigits = 4

CURRENT_POSITION = 0
OFFSET = 30.0
GUESS_OFFSET = 30.0

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\\frame0")

TRIES = 8


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Bull_and_cows_main_screen(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        # define some constants
        self.my_controller = None
        self.OFFSET_MENU = 30
        self.main_game_frame = tk.Frame(self)
        self.main_game_frame.pack()
        # self.window_main_screen = parent

        # # configure the root window
        # self.window_main_screen.geometry("1273x685")
        # self.window_main_screen.configure(bg="#F0F0F3")
        # self.window_main_screen.title("Bulls and Hits")
        self.NumberOfDigits = 4
        self.CURRENT_POSITION = 0
        self.GUESS_OFFSET = 30.0
        self.guess_counter = 0
        # create the canvas
        self.canvas = Canvas(
            self,
            bg="#F0F0F3",
            height=685,
            width=1573,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.pack(fill=tk.BOTH, expand=1)

        # create the blue menu on the left
        self.canvas.create_rectangle(0.0, 0.0, 276.0, 685.0, fill="#3A7FF6", outline="")
        self.canvas.create_text(13.0, 8.0, anchor="nw", text="Menu:", fill="#FF738E", font=("Inter Regular", 32 * -1))

        # create the orange canvas on the right
        self.orange_canvas = self.canvas.create_rectangle(900.0, 0.0, 1573.0, 685.0, fill="#FFA53C", outline="")
        self.canvas.create_text(920.0, 8.0, anchor="nw", text="Guesses:", fill="#7e37ad",
                                font=("Inter Regular", 32 * -1))

        # create the text area and scrollbar
        self.text_frame = tk.Frame(self.canvas, bg="#FFA53C", bd=0, highlightthickness=0)
        self.text_frame.place(x=910, y=50, width=650, height=600)

        self.text = tk.Text(self.text_frame, bg="#FFA53C", bd=0, highlightthickness=0, wrap="word", width=50)
        self.text.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self.text_frame, orient="vertical", command=self.text.yview, width=20)
        self.scrollbar.pack(side="right", fill="y")

        self.text.config(yscrollcommand=self.scrollbar.set, state='disabled')
        self.text['yscrollcommand'] = self.scrollbar.set

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
        entry_image_guess_1 = PhotoImage(file=relative_to_assets("entry_2.png"))
        self.entry_bg_guess_1 = self.canvas.create_image(330.0, 143.05126953125, image=entry_image_guess_1)
        self.entry_guess_1 = Entry(self.canvas, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font='Georgia 20')
        self.entry_guess_1.place(x=294.0, y=108.0, width=72.0, height=68.1025390625)

        self.entry_image_guess_2 = PhotoImage(file=relative_to_assets("entry_3.png"))
        self.entry_bg_guess_2 = self.canvas.create_image(419.5, 143.05126953125, image=self.entry_image_guess_2)
        self.entry_guess_2 = Entry(self.canvas, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font='Georgia 20')
        self.entry_guess_2.place(x=384.0, y=108.0, width=71.0, height=68.1025390625)

        self.entry_image_guess_3 = PhotoImage(file=relative_to_assets("entry_4.png"))
        self.entry_bg_guess_3 = self.canvas.create_image(508.5, 143.05126953125, image=self.entry_image_guess_3)
        self.entry_guess_3 = Entry(self.canvas, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font='Georgia 20')
        self.entry_guess_3.place(x=473.0, y=108.0, width=71.0, height=68.1025390625)

        self.entry_image_guess_4 = PhotoImage(file=relative_to_assets("entry_5.png"))
        self.entry_bg_guess_4 = self.canvas.create_image(601.0, 143.05126953125, image=self.entry_image_guess_4)
        self.entry_guess_4 = Entry(self.canvas, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font='Georgia 20')
        self.entry_guess_4.place(x=565.0, y=108.0, width=72.0, height=68.1025390625)

        # List of the guesses TextBoxes
        self.ENTRY_LIST = [self.entry_guess_1, self.entry_guess_2, self.entry_guess_3, self.entry_guess_4]

        # Text labels: Bulls, Hits
        self.canvas.create_text(310.0, 271.0, anchor="nw", text="Hits:", fill="#FF738E",
                                font=("Inter Regular", 32 * -1))
        self.entry_hits = Entry(self.canvas, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font='Georgia 13')
        self.entry_hits.place(x=405.0, y=273.0, width=30.0, height=30.0)

        self.canvas.create_text(310.0, 209.0, anchor="nw", text="Bulls:", fill="#FF738E",
                                font=("Inter Regular", 32 * -1))
        self.entry_bulls = Entry(self.canvas, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font='Georgia 13')
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

        self.button_image_Guess = PhotoImage(file=relative_to_assets("button_Guess.png"))
        self.button_Guess = Button(self.canvas, image=self.button_image_Guess, borderwidth=0, highlightthickness=0,
                                   command=lambda: self.take_the_guess(), relief="flat")
        self.button_Guess.place(x=295.0, y=343.0, width=250.0, height=70.1025390625)

        self.button_image_new_game = PhotoImage(file=relative_to_assets("button_new_game.png"))
        self. button_new_game = Button(self.canvas, image=self.button_image_new_game, borderwidth=0, highlightthickness=0,
                                 command=lambda: self.my_controller.show_frame(1), relief="flat")
        self.button_new_game.place(x=13.0, y=23.0 + self.OFFSET_MENU, width=250.0, height=70.1025390625)

        # self.button_image_prev_game = PhotoImage(file=relative_to_assets("button_prev_game.png"))
        # self.button_prev_game = Button(image=self.button_image_prev_game, borderwidth=0, highlightthickness=0,
        #                           command=lambda: print("button_prev_game clicked"), relief="flat")
        # self.button_prev_game.place(x=13.0, y=108.0 + self.OFFSET_MENU, width=250.0, height=70.1025390625)
        #
        # self.button_image_settings = PhotoImage(file=relative_to_assets("button_settings.png"))
        # self.button_settings = Button(image=self.button_image_settings, borderwidth=0, highlightthickness=0,
        #                          command=lambda: print("button_settings clicked"), relief="flat")
        # self.button_settings.place(x=13.0, y=193.0 + self.OFFSET_MENU, width=250.0, height=70.1025390625)

        self.button_image_stats = PhotoImage(file=relative_to_assets("button_stats.png"))
        self.button_stats = Button(self.canvas, image=self.button_image_stats, borderwidth=0, highlightthickness=0,
                              command=lambda: self.my_controller.show_frame(2), relief="flat")
        self.button_stats.place(x=13.0, y=108.0 + self.OFFSET_MENU, width=250.0, height=70.1025390625)
        # self.button_stats.place(x=14.0, y=278.0 + self.OFFSET_MENU, width=250.0, height=70.1025390625)


        self.button_image_0 = PhotoImage(file=relative_to_assets("button_0.png"))
        self.button_0 = Button(self.canvas, image=self.button_image_0, borderwidth=0, highlightthickness=0,
                          command=lambda: self.update_current_guess_board(0), relief="flat")
        self.button_0.place(x=295.0, y=498.0, width=72.0, height=70.102539062)

        self.button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
        self.button_8 = Button(self.canvas, image=self.button_image_8, borderwidth=0, highlightthickness=0,
                               command=lambda: self.update_current_guess_board(8), relief="flat")
        self.button_8.place(x=564.0, y=590.0, width=71.0, height=70.1025390625)

        self.button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
        self.button_4 = Button(self.canvas, image=self.button_image_4, borderwidth=0, highlightthickness=0,
                          command=lambda: self.update_current_guess_board(4), relief="flat")
        self.button_4.place(x=654.0, y=498.0, width=71.0, height=70.1025390625)

        self.button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
        self.button_9 = Button(self.canvas, image=self.button_image_9, borderwidth=0, highlightthickness=0,
                          command=lambda: self.update_current_guess_board(9), relief="flat")
        self.button_9.place(x=654.0, y=590.0, width=71.0, height=70.1025390625)

        self.button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
        self.button_5 = Button(self.canvas, image=self.button_image_5, borderwidth=0, highlightthickness=0,
                          command=lambda: self.update_current_guess_board(5), relief="flat")
        self.button_5.place(x=294.0, y=590.0, width=72.0, height=70.1025390625)

        self.button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
        self.button_6 = Button(self.canvas, image=self.button_image_6, borderwidth=0, highlightthickness=0,
                          command=lambda: self.update_current_guess_board(6), relief="flat")
        self.button_6.place(x=384.0, y=590.0, width=71.0, height=70.1025390625)

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = Button(self.canvas, image=self.button_image_1, borderwidth=0, highlightthickness=0,
                          command=lambda: self.update_current_guess_board(1), relief="flat")
        self.button_1.place(x=386.0, y=498.0, width=71.0, height=70.1025390625)

        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.button_2 = Button(self.canvas, image=self.button_image_2, borderwidth=0, highlightthickness=0,
                          command=lambda: self.update_current_guess_board(2), relief="flat")
        self.button_2.place(x=475.0, y=498.0, width=71.0, height=70.1025390625)

        self.button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
        self.button_7 = Button(self.canvas, image=self.button_image_7, borderwidth=0, highlightthickness=0,
                          command=lambda: self.update_current_guess_board(7), relief="flat")
        self.button_7.place(x=474.0, y=590.0, width=71.0, height=70.1025390625)

        self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        self.button_3 = Button(self.canvas, image=self.button_image_3, borderwidth=0, highlightthickness=0,
                          command=lambda: self.update_current_guess_board(3), relief="flat")
        self.button_3.place(x=564.0, y=498.0, width=71.0, height=70.1025390625)

        self.clear_all()
    
    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.my_controller = controller

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def take_the_guess(self):
        self.current_guess = ""
        for entry in self.ENTRY_LIST:
            self.current_guess += entry.get()
        self.clear_only_entrys()
        self.guess_counter += 1

        self.my_controller.main_sends_guess(int(self.current_guess))

    # return tuple in this template:
    # ("MSG", -1(error)/0(in game)/1(win)/2(lose) , bulls, cows)
    def show_what_returned_from_guess(self, tup):
        if tup[1] == -1:
            self.guess_counter -= 1

        self.show_guess_text(f"\n\n {self.guess_counter}) Guess: {self.current_guess} Bulls: {tup[2]} Hits: {tup[3]} \n\t{tup[0]}")

        self.entry_bulls.config(state='normal')
        self.entry_bulls.delete(0, tk.END)
        self.entry_bulls.insert(0, f"{tup[2]}")
        self.entry_bulls.config(state='disabled')
        self.entry_hits.config(state='normal')
        self.entry_hits.delete(0, tk.END)
        self.entry_hits.insert(0, f"{tup[3]}")
        self.entry_hits.config(state='disabled')

        if 1 <= tup[1] <= 2:
            self.button_Guess.config(state="disabled")


    def clear_only_entrys(self):
        self.clear_guess_text()
        for entry in self.BULLS_HITS_LIST:
            entry.config(state='normal')
            entry.delete(0, tk.END)
            entry.insert(0, "?")
            entry.config(state='disabled')
        self.canvas.delete("text")

    def clear_all(self):
        self.button_Guess.config(state="normal")
        if self.my_controller != None:
            self.my_controller.main_view_asks_to_start_game(TRIES)
        self.clear_guess_text()
        for entry in self.BULLS_HITS_LIST:
            entry.config(state='normal')
            entry.delete(0, tk.END)
            entry.insert(0, "?")
            entry.config(state='disabled')
        self.canvas.delete("text")
        self.guess_counter = 0
        self.show_guess_text("")

    def clear_guess_text(self):
        self.CURRENT_POSITION = 0
        for entry in self.ENTRY_LIST:
            entry.config(state='normal')
            entry.delete(0, tk.END)
            entry.insert(0, "?")
            entry.config(state='disabled')

    def show_guess_text(self, text):
        if text == "":
            self.text.config(state='normal')
            self.text.delete("1.0", "end")
            self.text.config(state='disabled')
        self.text.config(state='normal', font='Inter 15')
        self.text.insert("1.0", text)
        self.text.config(state='disabled')

    def show_text(self, num):
        if self.ENTRY_LIST[self.CURRENT_POSITION] != "":
            self.ENTRY_LIST[self.CURRENT_POSITION].config(state='normal')
            self.ENTRY_LIST[self.CURRENT_POSITION].delete(0, tk.END)
            self.ENTRY_LIST[self.CURRENT_POSITION].config(state='disabled')

        self.ENTRY_LIST[self.CURRENT_POSITION].config(state='normal')
        self.ENTRY_LIST[self.CURRENT_POSITION].insert(0, num)
        self.ENTRY_LIST[self.CURRENT_POSITION].config(state='disabled')

    def update_current_guess_board(self, number):
        if self.CURRENT_POSITION >= NumberOfDigits:
            self.CURRENT_POSITION = 0
        self.show_text(number)
        self.CURRENT_POSITION += 1


