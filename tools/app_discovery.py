# tools/app_discovery.py
from difflib import get_close_matches
from pathlib import Path
# tools/app_discovery.py


START_MENU_PATHS = [
    Path(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs"),
    Path.home() / r"AppData\Roaming\Microsoft\Windows\Start Menu\Programs"
]

DESKTOP_PATHS = [
    Path.home() / "Desktop"
]
APP_CACHE = {}
SPECIAL_APPS = {
    "calculator": "calc.exe",
    "file explorer": "explorer.exe",
    "explorer": "explorer.exe",
    "settings": "ms-settings:",
    "microsoft store": "ms-windows-store:"
}
ALIASES = {
    "vscode": "visual studio code",
    "vs code": "visual studio code",

    "chrome": "google chrome",

    "cursor ai": "cursor",

    "calc": "calculator"
}
def build_app_cache():

    APP_CACHE.clear()

    search_paths = START_MENU_PATHS + DESKTOP_PATHS

    for root_path in search_paths:

        if not root_path.exists():
            continue

        for file in root_path.rglob("*"):

            if file.suffix.lower() in [".lnk", ".exe"]:

                name = file.stem.lower()

                APP_CACHE[name] = str(file)

    return APP_CACHE

def find_app(app_name):

    app_name = app_name.lower().strip()

    app_name = ALIASES.get(app_name, app_name)

    # Exact match
    if app_name in APP_CACHE:
        return APP_CACHE[app_name]

    # Contains match
    for name, path in APP_CACHE.items():

        if app_name in name:
            return path

    # Fuzzy match (last resort)
    matches = get_close_matches(
        app_name,
        APP_CACHE.keys(),
        n=1,
        cutoff=0.85
    )

    if matches:
        return APP_CACHE[matches[0]]

    return None