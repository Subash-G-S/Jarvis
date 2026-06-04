# tools/file_open_tools.py

import os
from pathlib import Path

SEARCH_LOCATIONS = [
    Path.home() / "Desktop",
    Path.home() / "Documents",
    Path.home() / "Downloads"
]


def open_file(file_name):

    file_name = file_name.lower()

    for location in SEARCH_LOCATIONS:

        if not location.exists():
            continue

        for item in location.rglob("*"):

            if file_name in item.name.lower():

                os.startfile(item)

                return f"Opening {item.name}"

    return "File not found."