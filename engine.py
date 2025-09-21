# Importing Libraries.
import sys
import os
import glob
import tcod as englib

DATA_FOLDER = "data" # Defining 'data' path.
FONT_FILE = os.path.join(DATA_FOLDER, "dejavu10x10_gs_tc.png")

def main():
    screen_width = 80
    screen_height = 50
    englib.console_set_custom_font(FONT_FILE, englib.FONT_TYPE_GRAYSCALE | englib.FONT_LAYOUT_TCOD) # Setting the basic layout of the game.
    englib.console_init_root(screen_width, screen_height, "python roguelike", False) # Sets the size, the title, and if the program will or not be in fullscreen
    while not englib.console_is_window_closed():
        # Sets buffer.
        englib.console_set_default_foreground(0, englib.white)
        englib.console_put_char(0, 1, 1, '@', englib.BKGND_NONE)
        englib.console_flush()
        # Sets exit button (ESC).
        key = englib.console_check_for_keypress()
        if key.vk == englib.KEY_ESCAPE:
            return True

__name__ = "__main__"
if __name__ == "__main__":
    main()