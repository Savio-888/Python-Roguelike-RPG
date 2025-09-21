# Importing Libraries.
import sys
import os
import glob
import tcod as englib
from input_handlers import handle_keys

DATA_FOLDER = "data" # Defining 'data' path.
FONT_FILE = os.path.join(DATA_FOLDER, "dejavu10x10_gs_tc.png")

def main():
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)


    englib.console_set_custom_font(FONT_FILE, englib.FONT_TYPE_GRAYSCALE | englib.FONT_LAYOUT_TCOD) # Setting the basic layout of the game.
    englib.console_init_root(screen_width, screen_height, "python roguelike", False) # Sets the size, the title, and if the program will or not be in fullscreen
    con = englib.console_new(screen_width, screen_height)
    # Sets keyboard and mouse variables.
    key = englib.Key()
    mouse = englib.Mouse()
    while not englib.console_is_window_closed():
        # Sets buffer.
        englib.sys_check_for_event(englib.EVENT_KEY_PRESS, key, mouse)
        englib.console_set_default_foreground(con, englib.white)
        englib.console_put_char(con, player_x, player_y, '@', englib.BKGND_NONE)
        englib.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
        englib.console_flush()

        action = handle_keys(key)

        move = action.get('move')
        exit = action.get("exit")
        fullscreen = action.get("fullscreen")

        if move: # making the character move.
            dx, dy = move
            player_x += dx
            player_y += dy
        if exit :
            return True
        if fullscreen:
            englib.console_set_fullscreen(not englib.console_is_fullscreen())
if __name__ == "__main__":
    main()