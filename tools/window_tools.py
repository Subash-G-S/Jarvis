import pygetwindow as gw


def minimize_window(window_name):

    windows = gw.getWindowsWithTitle(
        window_name
    )

    if not windows:

        return f"No window found: {window_name}"

    windows[0].minimize()

    return f"Minimized {window_name}"
def maximize_window(window_name):

    windows = gw.getWindowsWithTitle(
        window_name
    )

    if not windows:

        return f"No window found: {window_name}"

    windows[0].maximize()

    return f"Maximized {window_name}"
def activate_window(window_name):

    windows = gw.getWindowsWithTitle(
        window_name
    )

    if not windows:

        return f"No window found: {window_name}"

    windows[0].activate()

    return f"Activated {window_name}"
import pyautogui


def close_active_window():

    pyautogui.hotkey(
        "alt",
        "f4"
    )

    return "Closed active window"