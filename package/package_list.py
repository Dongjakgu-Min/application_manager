from adb.client import Client as AdbClient
from util.tool import get_device, connection_is_valid


def show_package_list(device):
    a = device.shell('pm list packages -s')
    connection_is_valid(device)

    for line in a.split('\n'):
        if len(line) is not 0:
            print('Package Name : {0}'.format(
                line.split(':')[-1].split('=')[-1]))

    input('\npress any key to continue...')


def show_package_by_name():
    name = input('Input Package Name : ')
    result = []

    for p in get_package_list(get_device()):
        if name in p:
            print(p)

    input('\npress any key to continue...')


def get_package_list(device):
    adb = device.shell('pm list packages -s')
    result = []

    for line in adb.split('\n'):
        if len(line) is not 0:
            result.append(line.split(':')[-1].split('=')[-1])

    return result


def find_package_by_name():
    name = input('Input Package Name : ')
    result = []

    for p in get_package_list(get_device()):
        if name in p:
            result.append(p)
    return result
