import controller
import stats_screen
from stats_screen import Bull_and_cows_stats_screen
from tkinter import *

class Main:
    def __init__(self):
        self.controller = controller
        self.stats_screen = stats_screen
        self.screen = Tk()
        self.screen.title("Bulls & Hits")
        self.screen.geometry("1273x685")
        self.screen.configure(bg="#F0F0F3")
        self.screen.resizable(False, False)
        self.bulls_and_cows_stats_screen = Bull_and_cows_stats_screen(self.screen)

    def run_stats(self):
        self.stats_screen.mainloop()

m = Main()
m.run_stats()

