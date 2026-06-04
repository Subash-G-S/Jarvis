# tools/app_tools.py

import os

from tools.app_discovery import find_app


SPECIAL_APPS = {
    "calculator": "calc.exe",
    "calc": "calc.exe",

    "file explorer": "explorer.exe",
    "explorer": "explorer.exe",

    "settings": "ms-settings:",

    "microsoft store": "ms-windows-store:"
}


def open_app(app_name):

    app_name = app_name.lower().strip()

    # Handle Windows special apps first
    if app_name in SPECIAL_APPS:

        target = SPECIAL_APPS[app_name]

        os.system(f'start "" "{target}"')

        return f"Opening {app_name}"

    # Search discovered apps
    app_path = find_app(app_name)

    if not app_path:
        return f"Could not find {app_name}"

    os.startfile(app_path)

    return f"Opening {app_name}"