import pyautogui


def volume_up():

    pyautogui.press("volumeup")

    return "Volume increased"


def volume_down():

    pyautogui.press("volumedown")

    return "Volume decreased"


def mute_volume():

    pyautogui.press("volumemute")

    return "Volume muted"


def unmute_volume():

    pyautogui.press("volumemute")

    return "Volume unmuted"