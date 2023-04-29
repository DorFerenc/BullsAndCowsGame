import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

# create a Tkinter window
root = tk.Tk()
root.geometry("800x600")

# create a text widget
text = tk.Text(root)
# text.pack(side="left", fill="y")

# create a canvas widget
canvas = tk.Canvas(text)
# canvas.pack(fill="both", expand=True)

# create a matplotlib figure
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
ax.set_title("Example Plot")

# add the figure to the canvas
# canvas.draw()
figure_x, figure_y, figure_w, figure_h = canvas.bbox("all")
figure_w, figure_h = int(figure_w), int(figure_h)
photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)
canvas.create_image(0, 0, image=photo, anchor="nw")
fig_canvas = FigureCanvasTkAgg(fig, master=photo)
fig_canvas.draw()
fig_photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)
fig_photo.tk_photoimage = fig_photo  # prevent garbage collection
fig_photo.blank()  # create transparent image
canvas.create_image(0, 0, image=fig_photo, anchor="nw")
canvas.create_window(0, 0, window=fig_canvas.get_tk_widget(), anchor="nw")

# add labels and spaces between the graphs
text.insert("end", "\n\nLabel 1\n\n")
text.window_create("end", window=canvas)

text.insert("end", "\n\nLabel 2\n\n")

# add a scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=text.yview)
scrollbar.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollbar.set)

# start the Tkinter event loop
root.mainloop()


def create_graphs(self, fig):
    # stats_screen = tk.Tk()
    # stats_screen.title("Scrollbar Widget Example")

    # # apply the grid layout
    # root.grid_columnconfigure(0, weight=1)
    # root.grid_rowconfigure(0, weight=1)

    # create the text widget
    text = tk.Text(self.canvas, height=40, width=60)
    text.grid(row=0, column=0, sticky=tk.EW)
    # text.place(x=100, y=100)

    # create a scrollbar widget and set its command to the text widget
    scrollbar = ttk.Scrollbar(self.canvas, orient='vertical', command=text.yview)
    scrollbar.grid(row=0, column=1, sticky=tk.NS)

    #  communicate back to the scrollbar
    text['yscrollcommand'] = scrollbar.set

    # Create a canvas to embed the plot
    canvas = FigureCanvasTkAgg(fig, master=self.canvas)
    canvas.draw()

    # get the plot as a base64 encoded string
    buf = BytesIO()
    canvas.print_figure(buf, format='png')
    data = base64.b64encode(buf.getbuffer()).decode('ascii')

    # insert the plot into the text widget
    photo = tk.PhotoImage(data=data)
    text.image_create(tk.END, image=photo)