import tkinter as tk
from pathlib import Path
from tkinter import ttk, IntVar, Button, PhotoImage, Scale, HORIZONTAL

from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\\frame0")


def relative_to_assets(path: str) -> Path:
    """
     Returns the path relative to the assets folder.

     :param path: The path to be converted to a path relative to the assets folder.
     :type path: str
     :return: A path object representing the path relative to the assets folder.
     :rtype: Path
     """
    return ASSETS_PATH / Path(path)


class Bull_and_cows_stats_screen(tk.Frame):
    """A class representing a statistics screen for the Bull and Cows game."""
    def __init__(self, parent):
        """
        Initializes the statistics screen frame.

        :param parent: The parent widget for this frame.
        :type parent: tk.Widget
        """
        tk.Frame.__init__(self, parent)
        # define some constants
        self.OFFSET_MENU = 30
        self.stats_screen_frame = tk.Frame(self)
        self.stats_screen_frame.pack()

        # create the canvas
        self.canvas = tk.Canvas(
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
        self.canvas.create_text(920.0, 8.0, anchor="nw", text="", fill="#7e37ad",
                                font=("Inter Regular", 32 * -1))

        self.game_img = PhotoImage(file=relative_to_assets("Picture1.png"))

        # create the text area and scrollbar
        self.text_frame = tk.Frame(self.canvas, bg="#FFA53C", bd=0, highlightthickness=0)
        self.text_frame.place(x=910, y=50, width=650, height=600)

        # Create a label with the image
        self.game_img_label = tk.Label(self.text_frame, image=self.game_img, bg="#FFA53C", bd=0, highlightthickness=0)
        self.game_img_label.pack()

        # create the title text
        self.canvas.create_text(
            294.0,
            23.0,
            anchor="nw",
            text="Simulation and Statistics",
            fill="#745FF2",
            font=("Inter Regular", 48 * -1)
        )

        # number of games scale and label
        self.value_number_of_games = IntVar()
        self.scale_num_of_games = Scale(self.canvas, variable=self.value_number_of_games, from_=10, to=500,
                                        orient=HORIZONTAL, length=350)
        self.scale_num_of_games.bind("<ButtonRelease-1>", self.update_num_of_games_value)
        self.scale_num_of_games.place(x=300, y=100)
        self.number_of_games_label = ttk.Label(self.canvas, text=f"Number of games {self.scale_num_of_games.get()}",
                                               foreground="#7C0AA4", font=("Inter Regular", 15 * -1))
        self.number_of_games_label.place(x=400, y=80)

        self.run_game_button = Button(self.canvas, text='Run Statistics!', command=self.run_game)
        self.run_game_button.place(x=700, y=115)

        # Create  the progress bar
        self.progress_bar = ttk.Progressbar(self.canvas, orient=HORIZONTAL, length=500)
        self.progress_bar.config(mode='determinate', maximum=100.0, value=0)
        self.progress_bar.place(x=300, y=160)

        # Side menu buttons
        self.button_image_new_game = PhotoImage(file=relative_to_assets("Human_Game.png"))
        self.button_new_game = Button(self.canvas, image=self.button_image_new_game, borderwidth=0,
                                      highlightthickness=0,
                                      command=lambda: self.my_controller.show_frame(1), relief="flat")
        self.button_new_game.place(x=13.0, y=23.0 + self.OFFSET_MENU, width=250.0, height=70.1025390625)

        self.button_image_try_me = PhotoImage(file=relative_to_assets("Computer_Game.png"))
        self.button_try_me = Button(image=self.button_image_try_me, borderwidth=0, highlightthickness=0,
                          command=lambda: self.my_controller.show_frame(2), relief="flat")
        self.button_try_me.place(x=13.0, y=108.0 + self.OFFSET_MENU, width=250.0, height=70.1025390625)

        self.button_image_stats = PhotoImage(file=relative_to_assets("Statistics.png"))
        self.button_stats = Button(self.canvas, image=self.button_image_stats, borderwidth=0, highlightthickness=0,
                              command=lambda: self.my_controller.show_frame(3), relief="flat")
        self.button_stats.place(x=13.0, y=193.0 + self.OFFSET_MENU, width=250.0, height=70.1025390625)

        self.create_graphs(None)  # open an empty graph

    def update_num_of_games_value(self, event):
        """
        Update the text of the number_of_games_label based on the value of scale_num_of_games.

        :param event: The event that triggered the function.
        :type event: Event
        :return: None
        :rtype: None
        """
        self.number_of_games_label.config(text=f"Number of games {self.scale_num_of_games.get()}")

    def run_game(self):
        """
        Runs the game statistics for the selected number of digits and games.
        Calls the controller to produce the game data.

        :return: None
        :rtype: None
        """
        self.my_controller.run_stats2(self.scale_num_of_games.get())

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return: None
        """
        self.my_controller = controller

    def show_text(self, text):
        """
        Displays the given text on the screen.
        If the text is empty, clears the text area.

        :param text: The text to display on the screen.
        :type text: str
        :return: None
        :rtype: None
        """
        if text == "":
            self.text.config(state='normal')
            self.text.delete("1.0", "end")
            self.text.config(state='disabled')
        self.text.config(state='normal')
        self.text.insert("1.0", text)
        self.text.config(state='disabled')

    def create_graphs(self, fig):
        """
         Creates a graph on the screen using the given Figure object.

         :param fig: The Figure object representing the graph to create.
         :type fig: matplotlib.figure.Figure
         :return: None
         :rtype: None
         """
        # create the inner canvas
        inner_canvas = tk.Canvas(self.canvas)
        inner_canvas.place(x=276, y=200, width=620, height=480)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(fig, inner_canvas)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, inner_canvas)

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update_progress_bar(self, value):
        """
        Updates the progress bar value and refreshes the canvas.

        :param value: The value to set the progress bar to.
        :type value: int
        :return: None
        :rtype: None
        """
        self.progress_bar["value"] = value
        self.progress_bar.update()
        # self.canvas.update_idletasks()
