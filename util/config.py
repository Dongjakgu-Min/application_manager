import os
from util.tool import input_int
from util.noti import err_printer, info_printer


def config_main():
    path = os.path.join(os.getcwd(), 'config')

    while True:
        print('\nchoose config setting : ')
        print('1. SKT')
        print('2. KT')
        print('3. LG')
        print('4. custom')
        print('5. back')
        i = input_int()

        if i is 1:
            package_list = get_config(os.path.join(path, 'skt'))
            break
        elif i is 2:
            package_list = get_config(os.path.join(path, 'kt'))
            break
        elif i is 3:
            package_list = get_config(os.path.join(path, 'lg'))
            break
        elif i is 4:
            custom_path = input('\nPlease input Absolute Path : ')
            package_list = get_config(custom_path)
            break
        elif i is 5:
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


def file_check(path):
    if not os.path.exists(path):
        error_printer('file_not_exist')
        return False
    if not os.path.isfile(path):
        error_printer('not_config')
        return False

    return True
