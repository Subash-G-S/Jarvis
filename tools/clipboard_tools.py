import pyperclip

clipboard_history = []


def read_clipboard():

    text = pyperclip.paste()

    return text if text else "Clipboard is empty."


def copy_to_clipboard(text):

    pyperclip.copy(text)

    clipboard_history.append(text)

    return "Copied to clipboard."


def clear_clipboard():

    pyperclip.copy("")

    return "Clipboard cleared."


def get_clipboard_history():

    if not clipboard_history:

        return "No clipboard history."

    return "\n".join(
        clipboard_history[-10:]
    )