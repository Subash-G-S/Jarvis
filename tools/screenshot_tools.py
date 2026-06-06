import os
import pyautogui

import subprocess
from datetime import datetime
import time


SCREENSHOT_DIR = "screenshots"

os.makedirs(
    SCREENSHOT_DIR,
    exist_ok=True
)


def take_screenshot():

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    file_path = os.path.join(
        SCREENSHOT_DIR,
        f"screenshot_{timestamp}.png"
    )

    image = pyautogui.screenshot()

    image.save(file_path)

    return f"Screenshot saved: {file_path}"
def open_latest_screenshot():

    files = [
        os.path.join(
            SCREENSHOT_DIR,
            f
        )
        for f in os.listdir(
            SCREENSHOT_DIR
        )
        if f.endswith(".png")
    ]

    if not files:

        return "No screenshots found."

    latest = max(
        files,
        key=os.path.getctime
    )

    os.startfile(latest)

    return f"Opened {latest}"
def timed_screenshot(seconds):

    time.sleep(seconds)

    return take_screenshot()