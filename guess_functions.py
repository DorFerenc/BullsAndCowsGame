from tkinter import *
NumberOfDigits = 4

CURRENT_POSITION = 0
# MAPPING_POSITION_TO_ENTRY = {(0, entry_guess_1), (1, entry_guess_2), (2, entry_guess_3), (3, entry_guess_4)}

def update_current_guess_board(number, entity_list):
    global CURRENT_POSITION
    # MAPPING_POSITION_TO_ENTRY[CURRENT_POSITION].insert(number)
    print(f"button_{number} clicked")
    entity_list[CURRENT_POSITION].insert(0, str(number))
    if CURRENT_POSITION != NumberOfDigits - 1:
        CURRENT_POSITION += 1

def take_the_guess(entry_list):
    guess = ""
    for entry in entry_list:
        guess += entry.get()
    for entry in entry_list:
        entry.delete(0, END)
    return guess
