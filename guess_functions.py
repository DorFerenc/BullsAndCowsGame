from tkinter import *
NumberOfDigits = 4

CURRENT_POSITION = 0
OFFSET = 30.0
# MAPPING_POSITION_TO_ENTRY = {(0, entry_guess_1), (1, entry_guess_2), (2, entry_guess_3), (3, entry_guess_4)}

def update_current_guess_board(number, entity_list):
    global CURRENT_POSITION
    # MAPPING_POSITION_TO_ENTRY[CURRENT_POSITION].insert(number)
    print(f"button_{number} clicked")
    entity_list[CURRENT_POSITION].insert(0, str(number))
    CURRENT_POSITION += 1
    if CURRENT_POSITION == NumberOfDigits:
        CURRENT_POSITION = 0

def take_the_guess(entry_list, canvas, bulls_hits_list):
    global OFFSET
    guess = ""
    for entry in bulls_hits_list:
        entry.delete(0, END)
    for entry in entry_list:
        guess += entry.get()
    for entry in entry_list:
        entry.delete(0, END)
    # for entry in bulls_hits_list:
    #     entry.insert(0, "2")
    OFFSET = OFFSET + 30.0
    canvas.create_text(920.0, OFFSET, anchor="nw", text="guess: " + guess + " bulls:" + bulls_hits_list[0].get() + " hits:" + bulls_hits_list[1].get(),
                       fill="#0d0c0c", font=('Georgia 15'))
    print(guess)
    return guess

def generate_secret_number():
    pass