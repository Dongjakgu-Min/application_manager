import subprocess
import sys


def show_package_list():
    a = subprocess.check_output(['adb', 'shell', 'pm', 'list', 'packages', '-s'], universal_newlines=True)

    for line in a.split('\n'):
        if len(line) is not 0:
            print('Package Name : {0}'.format(line.split(':')[-1].split('=')[-1]))

    input('\npress any key to continue...')


def show_package_by_name():
    name = input('Input Package Name : ')
    result = []

    for p in get_package_list():
        if name in p:
            print(p)

    input('\npress any key to continue...')


def get_package_list():
    adb = subprocess.check_output(['adb', 'shell', 'pm', 'list', 'packages', '-s'], universal_newlines=True)
    result = []

    for line in adb.split('\n'):
        if len(line) is not 0:
            result.append(line.split(':')[-1].split('=')[-1])

    return result


def find_package_by_name():
    name = input('Input Package Name : ')
    result = []

    for p in get_package_list():
        if name in p:
            result.append(p)
    
    return result

