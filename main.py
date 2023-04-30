import tkinter as tk

from controller import Controller
from model_graphs import Graph_Model
from main_game_screen import Bull_and_cows_main_screen
from bh_back import BH_back
from bh import BH

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo')

        # create a model
        model2 = BH_back

        # create a view and place it on the root window
        view2_screen_stats = Bull_and_cows_main_screen(self)
        # view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = Controller(model2, view2_screen_stats)

        # set the controller to view
        view2_screen_stats.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()

# self.screen = Tk()
# view1_screen_stats.title("Bulls & Hits")
# view1_screen_stats.geometry("1273x685")
# view1_screen_stats.configure(bg="#F0F0F3")
# view1_screen_stats.resizable(False, False)