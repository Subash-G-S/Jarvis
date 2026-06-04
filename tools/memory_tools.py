# tools/memory_tools.py

import os

from agent.memory import MEMORY


def open_last_file():

    path = MEMORY["last_file"]

    if not path:
        return "No file remembered."

    os.startfile(path)

    return f"Opening {path}"
def get_last_file():

    return MEMORY["last_file"]