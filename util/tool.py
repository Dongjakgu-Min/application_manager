from .noti import err_printer
from pathlib import Path
from package import disable_package


def input_int():
    try:
        choice = int(input('input number what you want to do : '))
    except ValueError:
        choice = None
    return choice


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


def write_list(packages):
    result = list()

    while True:
        _str = input('\n> ')

        if _str == '/END':
            break
        elif _str == '/MODE':
            packages.change_mode()

        if len(_str) is 0:
            continue

        items = packages.find(_str)

        # print(items == _str)
        if len(items) is 1 and items[0]['package'] == _str:
            result += items if items not in items else None
        else:
            for i in items:
                if i['label'] is None:
                    print("{0}".format(i['package']))
                else:
                    print("{0} ({1})".format(i['package'], i['label']))

    return result
