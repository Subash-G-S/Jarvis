_last_file = None


def set_last_file(filepath):

    global _last_file

    _last_file = filepath


def get_last_file():

    return _last_file