from util.tool import input_int, file_check, connection_is_valid
from util.noti import err_printer, info_printer
from package.package_list import make_package_list
from pathlib import Path


def config_main(device):
    path = Path.cwd() / 'config'

    while True:
        print('\nchoose config setting : ')
        print('1. SKT')
        print('2. KT')
        print('3. LG')
        print('4. custom')
        print('5. create config file')
        print('6. manual mode')
        print('99. back')
        i = input_int()

        if i is 1:
            package_list = get_config(path / 'skt')
            break
        elif i is 2:
            package_list = get_config(path / 'kt')
            break
        elif i is 3:
            package_list = get_config(path / 'lg')
            break
        elif i is 4:
            custom_path = input('\nPlease input Absolute Path : ')
            package_list = get_config(custom_path)
            break
        elif i is 5:
            valid = connection_is_valid(device)
            make_package_list(valid)
            return None
        elif i is 6:
            return 'Manual'
        elif i is 99:
            return None
        else:
            print('Invalid Input!')
    return package_list


def get_config(path):
    while True:
        check = file_check(path)
        if check is True:
            break
        path = input('\nPlease input Absolute Path : ')
    with open(path) as f:
        result = f.read().splitlines()

    return result
