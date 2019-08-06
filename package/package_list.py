from adb.client import Client as AdbClient
from util.tool import get_device, connection_is_valid, get_package_information
from util.init import get_package_label


def show_package_list(device):
    a = device.shell('pm list packages -s -f')
    connection_is_valid(device)

    for line in a.split('\n'):
        if len(line) is not 0:
            package_name, package_path = get_package_information(line)
            package_label = get_package_label(package_path)
            print('Package Name : {0}, Package Label : {1}'.format(package_name, package_label))

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
