import tkinter as tk

from controller import Controller
from model_graphs import Graph_Model
from main_game_screen import Bull_and_cows_main_screen
from bh_back import BH_back
from bh import BH
from stats_screen import Bull_and_cows_stats_screen


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # self.title('Tkinter MVC Demo')
        self.geometry("1573x685")
        self.configure(bg="#F0F0F3")
        self.resizable(False, False)

        self.title("Bulls and Hits")

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # self.frames = {} # initializing frames to an empty array
        #
        # # iterating through a tuple consisting of the different page layouts
        # for F in (Bull_and_cows_main_screen, Bull_and_cows_stats_screen):
        #     frame = F(container)
        #     frame.set_controller(self)
        #     self.frames[F] = frame
        #     frame.grid(row=0, column=0, sticky="nsew")

        # create model's
        model_play_game = BH_back()
        model_graph = Graph_Model()
        model_bh_orig = BH()

        # create a controller
        Controller(model_play_game, model_graph, model_bh_orig, container)


        # # to display the current frame passed as
        # # parameter
        # def show_frame(self, cont):
        #     frame = self.frames[cont]
        #     frame.tkraise()

if __name__ == '__main__':
    app = App()
    app.mainloop()

# self.screen = Tk()
# view1_screen_stats.title("Bulls & Hits")
# view1_screen_stats.geometry("1273x685")
# view1_screen_stats.configure(bg="#F0F0F3")
# view1_screen_stats.resizable(False, False)

# # create a view and place it on the root window
# view1_screen_stats = Bull_and_cows_stats_screen(self)
# view2_main_screen = Bull_and_cows_main_screen(self)
#
# # set the controller to view
# view1_screen_stats.set_controller(controller)
# view2_main_screen.set_controller(controller)