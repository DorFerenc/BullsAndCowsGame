from main_game_play import entry_guess_1, entry_guess_2, entry_guess_3, entry_guess_4
from bh import *

CURRENT_POSITION = 0
MAPPING_POSITION_TO_ENTRY = {(0, entry_guess_1), (1, entry_guess_2), (2, entry_guess_3), (3, entry_guess_4)}

def update_current_guess_board(number):
    global CURRENT_POSITION
    MAPPING_POSITION_TO_ENTRY[CURRENT_POSITION].insert(number)
    if CURRENT_POSITION != NumberOfDigits - 1:
        CURRENT_POSITION += 1
