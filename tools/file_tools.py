from pathlib import Path

def create_folder(folder_name):
    desktop = Path.home() / "Desktop"

    new_folder = desktop / folder_name

    new_folder.mkdir(exist_ok=True)

    return f"Folder '{folder_name}' created successfully."

def create_file(file_name):

    desktop = Path.home() / "Desktop"

    file_path = desktop / file_name

    file_path.touch(exist_ok=True)

    return f"{file_name} created successfully."
from send2trash import send2trash

def delete_file(file_name):

    desktop = Path.home() / "Desktop"

    file_path = desktop / file_name

    if not file_path.exists():
        return "File not found."

    send2trash(str(file_path))

    return f"{file_name} moved to recycle bin."
SEARCH_LOCATIONS = [
    Path.home() / "Desktop",
    Path.home() / "Documents",
    Path.home() / "Downloads"
]


def rename_file(old_name, new_name):

    old_name = old_name.lower()

    for location in SEARCH_LOCATIONS:

        if not location.exists():
            continue

        for item in location.rglob("*"):

            if item.name.lower() == old_name:

                new_path = item.parent / new_name

                item.rename(new_path)

                return f"Renamed {old_name} to {new_name}"

    return "File not found."
from services.file_memory import (
    get_last_file
)


def get_last_generated_file():

    filepath = get_last_file()

    if not filepath:

        return "No file available."

    return filepath