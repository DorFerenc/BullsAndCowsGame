import tkinter as tk
from tkinter import ttk

from main_game_screen import Bull_and_cows_main_screen
from stats_screen import Bull_and_cows_stats_screen


# class Model:
#     def __init__(self):
#         self.data = "Hello, World!"
#
# class View1(ttk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#
#         self.controller = controller
#         self.label = tk.Label(self, text="This is View 1")
#         self.label.pack(pady=50)
#         self.button = tk.Button(self, text="Switch to View 2", command=self.controller.show_view2)
#         self.button.pack()
#
#
# class View2(ttk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         self.controller = controller
#         self.label = tk.Label(self, text="This is View 2")
#         self.label.pack(pady=50)
#         self.button = tk.Button(self, text="Switch to View 1", command=self.controller.show_view1)
#         self.button.pack()
#
#
# class Controller:
#     def __init__(self, root):
#         self.model = Model()
#         self.root = root
#         # self.root.geometry("400x300")
#
#
#         self.view1 = Bull_and_cows_stats_screen(self.root)
#         self.view2 = Bull_and_cows_main_screen(self.root)
#         # self.view1 = Bull_and_cows_stats_screen(root)
#
#         self.view1.set_controller(self)
#         self.view2.set_controller(self)
#
#         # self.view1.pack()
#         # self.view2.pack()
#         self.show_view2()
#
#     def show_view1(self):
#         self.view1.pack()
#         self.view2.pack_forget()
#
#     def show_view2(self):
#         self.view2.pack()
#         self.view1.pack_forget()





LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("1573x685")
        self.configure(bg="#F0F0F3")
        self.resizable(False, False)
        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Bull_and_cows_main_screen, Bull_and_cows_stats_screen):
            frame = F(container)
            frame.set_controller(self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Bull_and_cows_main_screen)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



if __name__ == "__main__":
    # root = tk.Tk()
    # app = Controller(root)
    # root.mainloop()

    # Driver Code
    app = tkinterApp()
    app.mainloop()