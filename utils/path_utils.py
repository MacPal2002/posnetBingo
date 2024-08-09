# utils/path_utils.py
import sys
import os


def resource_path(relative_path):
    try:
        # Attempt to access the _MEIPASS attribute set by PyInstaller
        base_path = sys._MEIPASS  # type:ignore
    except AttributeError:
        # _MEIPASS does not exist; fallback to the current directory
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def file_exit(filename):
    if os.path.isfile(filename):
        return True
    else:
        return False


def is_empty(filename):
    if os.path.getsize(filename) == 0:
        return True
    else:
        return False
