
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from guess_functions import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\\frame0") #Path(r"C:\Users\dorfe\PycharmProjects\Tkinter-Designer\build\assets\frame0")
OFFSET_MENU = 30


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1273x685")
window.configure(bg = "#F0F0F3")


canvas = Canvas(
    window,
    bg = "#F0F0F3",
    height = 685,
    width = 1273,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(0.0, 0.0, 276.0, 685.0, fill="#3A7FF6", outline="") #blue canvas right
canvas.create_text(13.0, 8.0, anchor="nw", text="Menu:", fill="#FF738E", font=("Inter Regular", 32 * -1))

orange_canvas = canvas.create_rectangle(900.0, 0.0, 1273.0, 685.0, fill="#FFA53C", outline="") #orange canvas left
canvas.create_text(920.0, 8.0, anchor="nw", text="Guesses:", fill="#7e37ad", font=("Inter Regular", 32 * -1))


canvas.create_text(
    294.0,
    23.0,
    anchor="nw",
    text="Bulls and Hits",
    fill="#745FF2",
    font=("Inter Regular", 48 * -1)
)

entry_image_guess_1 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_guess_1 = canvas.create_image(330.0, 143.05126953125, image=entry_image_guess_1)
entry_guess_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=('Georgia 20'))
entry_guess_1.place(x=294.0, y=108.0, width=72.0, height=68.1025390625)

entry_image_guess_2 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_guess_2 = canvas.create_image(419.5, 143.05126953125, image=entry_image_guess_2)
entry_guess_2 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=('Georgia 20'))
entry_guess_2.place(x=384.0, y=108.0, width=71.0, height=68.1025390625)

entry_image_guess_3 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_guess_3 = canvas.create_image(508.5, 143.05126953125, image=entry_image_guess_3)
entry_guess_3 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=('Georgia 20'))
entry_guess_3.place(x=473.0, y=108.0, width=71.0, height=68.1025390625)

entry_image_guess_4 = PhotoImage(file=relative_to_assets("entry_5.png"))
entry_bg_guess_4 = canvas.create_image(601.0, 143.05126953125, image=entry_image_guess_4)
entry_guess_4 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=('Georgia 20'))
entry_guess_4.place(x=565.0, y=108.0, width=72.0, height=68.1025390625)

ENTRY_LIST = [entry_guess_1, entry_guess_2, entry_guess_3, entry_guess_4]

canvas.create_text(310.0, 271.0, anchor="nw", text="Hits:", fill="#FF738E", font=("Inter Regular", 32 * -1))
entry_hits = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=('Georgia 13'))
entry_hits.place(x=405.0, y=273.0, width=30.0, height=30.0)

canvas.create_text(310.0, 209.0, anchor="nw", text="Bulls:", fill="#FF738E", font=("Inter Regular", 32 * -1))
entry_bulls = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=('Georgia 13'))
entry_bulls.place(x=405.0, y=211.0, width=30.0, height=30.0)

BULLS_HITS_LIST = [entry_bulls, entry_hits]

canvas.create_text(
    607.0,
    220.0,
    anchor="nw",
    text="matching digits in the right positions",
    fill="#7B0AA3",
    font=("Inter Regular", 15 * -1)
)

canvas.create_text(
    607.0,
    282.0,
    anchor="nw",
    text="matching digits in different positions",
    fill="#7C0AA4",
    font=("Inter Regular", 15 * -1)
)

button_image_Guess = PhotoImage(file=relative_to_assets("button_Guess.png"))
button_Guess = Button(image=button_image_Guess, borderwidth=0, highlightthickness=0,
                      command=lambda: take_the_guess(ENTRY_LIST, canvas, BULLS_HITS_LIST), relief="flat")
button_Guess.place(x=295.0, y=343.0, width=250.0, height=70.1025390625)

button_image_new_game = PhotoImage(file=relative_to_assets("button_new_game.png"))
button_new_game = Button(image=button_image_new_game, borderwidth=0, highlightthickness=0,
                         command=lambda: print("button_new_game clicked"), relief="flat")
button_new_game.place(x=13.0, y=23.0 + OFFSET_MENU, width=250.0, height=70.1025390625)

button_image_prev_game = PhotoImage(file=relative_to_assets("button_prev_game.png"))
button_prev_game = Button(image=button_image_prev_game, borderwidth=0, highlightthickness=0,
                          command=lambda: print("button_prev_game clicked"), relief="flat")
button_prev_game.place(x=13.0, y=108.0 + OFFSET_MENU, width=250.0, height=70.1025390625)

button_image_settings = PhotoImage(file=relative_to_assets("button_settings.png"))
button_settings = Button(image=button_image_settings, borderwidth=0, highlightthickness=0,
                         command=lambda: print("button_settings clicked"), relief="flat")
button_settings.place(x=13.0, y=193.0 + OFFSET_MENU, width=250.0, height=70.1025390625)

button_image_stats = PhotoImage(file=relative_to_assets("button_stats.png"))
button_stats = Button(image=button_image_stats, borderwidth=0, highlightthickness=0,
                      command=lambda: print("button_stats clicked"), relief="flat")
button_stats.place(x=14.0, y=278.0 + OFFSET_MENU, width=250.0, height=70.1025390625)


button_image_0 = PhotoImage(file=relative_to_assets("button_0.png"))
button_0 = Button(image=button_image_0, borderwidth=0, highlightthickness=0,
                  command=lambda: update_current_guess_board(0, ENTRY_LIST), relief="flat")
button_0.place(x=295.0, y=498.0, width=72.0, height=70.102539062)

button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
button_8 = Button(image=button_image_8, borderwidth=0, highlightthickness=0,
                  command=lambda: update_current_guess_board(8, ENTRY_LIST), relief="flat")
button_8.place(x=564.0, y=590.0, width=71.0, height=70.1025390625)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(image=button_image_4, borderwidth=0, highlightthickness=0,
                  command=lambda: update_current_guess_board(4, ENTRY_LIST), relief="flat")
button_4.place(x=654.0, y=498.0, width=71.0, height=70.1025390625)

button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
button_9 = Button(image=button_image_9, borderwidth=0, highlightthickness=0,
                  command=lambda: update_current_guess_board(9, ENTRY_LIST), relief="flat")
button_9.place(x=654.0, y=590.0, width=71.0, height=70.1025390625)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(image=button_image_5, borderwidth=0, highlightthickness=0,
                  command=lambda: update_current_guess_board(5, ENTRY_LIST), relief="flat")
button_5.place(x=294.0, y=590.0, width=72.0, height=70.1025390625)

button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
button_6 = Button(image=button_image_6, borderwidth=0, highlightthickness=0,
                  command=lambda: update_current_guess_board(6, ENTRY_LIST), relief="flat")
button_6.place(x=384.0, y=590.0, width=71.0, height=70.1025390625)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0,
                  command=lambda: update_current_guess_board(1, ENTRY_LIST), relief="flat")
button_1.place(x=386.0, y=498.0, width=71.0, height=70.1025390625)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0,
                  command=lambda: update_current_guess_board(2, ENTRY_LIST), relief="flat")
button_2.place(x=475.0, y=498.0, width=71.0, height=70.1025390625)

button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
button_7 = Button(image=button_image_7, borderwidth=0, highlightthickness=0,
                  command=lambda: update_current_guess_board(7, ENTRY_LIST), relief="flat")
button_7.place(x=474.0, y=590.0, width=71.0, height=70.1025390625)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0,
                  command=lambda: update_current_guess_board(3, ENTRY_LIST), relief="flat")
button_3.place(x=564.0, y=498.0, width=71.0, height=70.1025390625)

window.resizable(False, False)
window.mainloop()
