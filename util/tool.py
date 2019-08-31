from .noti import err_printer
from pathlib import Path


def input_int():
    try:
        choice = int(input('input number what you want to do : '))
    except ValueError:
        choice = None
    return choice


def config_writer(data):
    result = '\n'.join(data)
    return result


def dir_check(path):
    if path.is_dir() is False:
        Path.mkdir(path)

    return path


def file_check(path):
    if not Path(path).exists:
        err_printer('file_not_exist')
        return False
    if not Path(path).is_dir:
        err_printer('not_config')
        return False

    return True
