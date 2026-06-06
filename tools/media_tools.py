import pyautogui


def play_pause():

    pyautogui.press("playpause")

    return "Media toggled"


def next_track():

    pyautogui.press("nexttrack")

    return "Next track"


def previous_track():

    pyautogui.press("prevtrack")

    return "Previous track"