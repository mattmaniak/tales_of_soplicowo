"""Keyboard and mouse handling."""

import sys

try:
    from panda3d.core import WindowProperties
except ModuleNotFoundError:
    sys.stderr.write("Panda3d not found.\n")
    exit()


MOUSE_SENSITIVITY_DEG = 60
KEYPRESS_TIMEOUT_S = 0.1

pressed_keys = {'w': False,
                's': False,
                'a': False,
                'd': False,
                "lshift": False,
                "lcontrol": False}

mouse_pos = {'x': 0, 'y': 0}


class Keymap:
    """Keyboard bindings."""

    class Player:
        """Player steering."""

        go_forward = 'w'
        go_backward = 's'
        go_left = 'a'
        go_right = 'd'
        toggle_run = "lshift"
        toggle_crouch = "lcontrol"


def handle_events():
    """Wrap keyboard and mouse calls."""

    __poll_keyboard()
    __assign_mouse_pos()


def limit_mouse_pos(min_pitch_deg: float, max_pitch_deg: float):
    """
    Panda3D describes max. left mouse position as x = -1 and max. right
    as the x = 1. The same thing is with the Y axis. If You move the
    mouse a lot, the values can be relatively smaller and bigger, e.g.
    y = 6.35. This method set the mouse position to avoid such values.

    Parameters:
    min_pitch_deg -- how low can You look.
    max_pitch_deg -- how far can You look on the sky.
    """

    global MOUSE_SENSITIVITY_DEG
    global mouse_pos

    DEFAULT_POINTER_ID = 0
    window = base.win.getProperties()

    # Convert P3D coorinates to screen pixels.
    mouse_x_onscreen_px = (window.getXSize() / 2) + ((window.getXSize() / 2)
                                                     * mouse_pos['x'])

    mouse_y_onscreen_px = (window.getYSize() / 2) - ((window.getYSize() / 2)
                                                     * mouse_pos['y'])

    # Push the mouse pointer maximally to the left.
    if -mouse_pos['x'] * MOUSE_SENSITIVITY_DEG < 0:
        mouse_x_onscreen_px = (window.getXSize() / 2) \
            - (window.getXSize() / 2 * 360 / MOUSE_SENSITIVITY_DEG)

    # Push the pointer to the default pos (center).
    elif -mouse_pos['x'] * MOUSE_SENSITIVITY_DEG > 360:
        mouse_x_onscreen_px = window.getXSize() / 2

    # Mouse is too low.
    if mouse_pos['y'] * MOUSE_SENSITIVITY_DEG < min_pitch_deg:
        mouse_y_onscreen_px = (window.getYSize() / 2) \
            - (window.getYSize() / 2 * min_pitch_deg /
               MOUSE_SENSITIVITY_DEG)

    # Mouse is too high.
    elif mouse_pos['y'] * MOUSE_SENSITIVITY_DEG > max_pitch_deg:
        # Konwersja pandowych koordynatów myszy na piksele na ekranie.
        mouse_y_onscreen_px = (window.getYSize() / 2) \
            - (window.getYSize() / 2 * max_pitch_deg /
               MOUSE_SENSITIVITY_DEG)

    base.win.movePointer(DEFAULT_POINTER_ID, int(mouse_x_onscreen_px),
                         int(mouse_y_onscreen_px))


def setup_mouse():
    """
    Set the mouse mode from the absolute to the relative
    (RPG-games-like).
    """

    # https://docs.panda3d.org/1.10/python/programming/hardware-support/mouse-support#relative-mouse-mode
    new_mouse_settings = WindowProperties()
    base.disableMouse()  # Disable default mouse steering.
    new_mouse_settings.setCursorHidden(True)

    # Enable infinite in-game mouse movement.
    new_mouse_settings.setMouseMode(WindowProperties.M_relative)
    base.win.requestProperties(new_mouse_settings)


def __assign_mouse_pos():
    """
    Store the mouse pos values in variables those will be used in
    another modules.
    """

    global mouse_pos

    if base.mouseWatcherNode.hasMouse():
        mouse = base.mouseWatcherNode.getMouse()

        mouse_pos['x'] = mouse.getX()
        mouse_pos['y'] = mouse.getY()


def __poll_keyboard():
    """Look for keyboard events."""

    global pressed_keys

    for key in pressed_keys:
        if base.mouseWatcherNode.is_button_down(key):
            __set_key_state(key, "down")
        else:
            __set_key_state(key, "up")
    base.accept("escape", sys.exit)


def __set_key_state(key: str, state: str):
    """Set the key state to up or down.

    Parameters:
    key -- key name, e.g. 'w' or 'S'.
    state -- just "up" or "down".
    """

    global pressed_keys

    if state == "down":
        pressed_keys[key] = True
    elif state == "up":
        pressed_keys[key] = False
