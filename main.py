import tk as tk

import controller
import stats_screen
from bh import BH
from controller import Controller
from stats_screen import Bull_and_cows_stats_screen
from tkinter import *
import tkinter as tk
#
# class Main:
#     def __init__(self):
#         self.controller = controller
#         self.stats_screen = stats_screen
#         self.screen = Tk()
#         self.screen.title("Bulls & Hits")
#         self.screen.geometry("1273x685")
#         self.screen.configure(bg="#F0F0F3")
#         self.screen.resizable(False, False)
#         self.bulls_and_cows_stats_screen = Bull_and_cows_stats_screen(self.screen)
#
#     def run_stats(self):
#         self.stats_screen.mainloop()
#
# m = Main()
# m.run_stats()

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo')

        # create a model
        model = None

        # create a view and place it on the root window
        view1_screen_stats = Bull_and_cows_stats_screen(self)
        # view.grid(row=0, column=0, padx=10, pady=10)
        # self.screen = Tk()
        # view1_screen_stats.title("Bulls & Hits")
        # view1_screen_stats.geometry("1273x685")
        # view1_screen_stats.configure(bg="#F0F0F3")
        # view1_screen_stats.resizable(False, False)

        # create a controller
        controller = Controller(model, view1_screen_stats)

        # set the controller to view
        view1_screen_stats.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()