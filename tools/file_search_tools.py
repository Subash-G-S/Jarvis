from pathlib import Path
from agent.memory import MEMORY
SEARCH_LOCATIONS = [
    Path.home() / "Desktop",
    Path.home() / "Documents",
    Path.home() / "Downloads"
]


def search_files(keyword):

    keyword = keyword.lower()

    matches = []

    for location in SEARCH_LOCATIONS:

        if not location.exists():
            continue

        for item in location.rglob("*"):

            if keyword in item.name.lower():

                matches.append(str(item))

    # SAVE TO MEMORY
    MEMORY["last_search_results"] = matches

    if matches:
        MEMORY["last_file"] = matches[0]

    if not matches:
        return "No matching files found."

    return "\n".join(matches[:10])