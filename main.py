import tkinter as tk

from bh_back import BH_back
from controller import Controller
from model_graphs import Graph_Model


class App(tk.Tk):
    """The main application window for the Bulls and Hits game."""
    def __init__(self):
        super().__init__()

        # configure the root window
        self.geometry("1573x685")
        self.configure(bg="#F0F0F3")
        self.resizable(False, False)
        self.title("Bulls and Hits")

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # create model's
        model_play_game = BH_back()
        model_graph = Graph_Model()
        # model_bh_orig = BH()

        # create a controller
        Controller(model_play_game, model_graph, container)


if __name__ == '__main__':
    app = App()
    app.mainloop()
