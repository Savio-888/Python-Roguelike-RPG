import tcod as englib
def handle_keys(key):
    # Movement Keys
    if key.vk == englib.KEY_UP:
        return {"move":(0, -1)}
    elif key.vk == englib.KEY_DOWN:
        return {"move":(0, 1)}
    elif key.vk == englib.KEY_LEFT:
        return {"move":(-1, 0)}
    elif key.vk == englib.KEY_RIGHT:
        return {"move":(1, 0)}
    # Toggle Fullscreen
    if key.vk == englib.KEY_ENTER and key.lalt:
        return {"fullscreen": True}
    elif key.vk == englib.KEY_ESCAPE:
        return True