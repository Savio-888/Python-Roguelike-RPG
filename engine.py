# Importing Libraries.
import sys
import os
import glob
import tcod as libtcod
from input_handlers import handle_keys

DATA_FOLDER = "data" # Defining 'data' path.
FONT_FILE = os.path.join(DATA_FOLDER, "dejavu10x10_gs_tc.png")

def main():
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)


    libtcod.console_set_custom_font(FONT_FILE, libtcod.FONT_TYPE_GRAYSCALE | libtcod.FONT_LAYOUT_TCOD) # Setting the basic layout of the game.
    libtcod.console_init_root(screen_width, screen_height, "python roguelike", False) # Sets the size, the title, and if the program will or not be in fullscreen
    con = libtcod.console_new(screen_width, screen_height)
    # Sets keyboard and mouse variables.
    key = libtcod.Key()
    mouse = libtcod.Mouse()
    while not libtcod.console_is_window_closed():
        # Sets buffer.
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        libtcod.console_set_default_foreground(con, libtcod.white)
        libtcod.console_put_char(con, player_x, player_y, '@', libtcod.BKGND_NONE) # puts main character (no pun intended) on screen.
        libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
        libtcod.console_flush()

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
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
if __name__ == "__main__":
    main()