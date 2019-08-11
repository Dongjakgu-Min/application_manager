from adb.client import Client as AdbClient
from util.tool import connection_is_valid, get_package_information, check_connection, config_writer, check_aapt
from util.noti import info_printer, err_printer
from pathlib import Path


def show_package_list(device):
    valid_device = connection_is_valid(device)
    check_aapt(valid_device)
    a = valid_device.shell('pm list packages -s -f')

    for line in a.split('\n'):
        if len(line) is not 0:
            package_name, package_label = get_package_information(line)
            if package_label is None:
                print('Package Name : {0}'.format(package_name))
            else:
                print('Package Name : {0}, Package Label : {1}'.format(
                    package_name, package_label))

    input('\npress any key to continue...')


def show_package_by_name(device):
    name = input('Input Package Name : ')
    result = []

    valid_device = connection_is_valid(device)

    for p in get_package_list(valid_device):
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


def find_package_by_name(device):
    name = input('Input Package Name : ')
    result = []

    valid_device = connection_is_valid(device)

    for p in get_package_list(valid_device):
        if name in p:
            result.append(p)
    return result


def make_package_list(device):
    valid_device = connection_is_valid(device)
    # show_package_list(valid_device)
    package_list = list()

    info_printer('config_write_info')
    config_name = str(input('Please Input config file name : '))

    config_descriptor = Path(Path.cwd() / 'config' /
                             config_name).open('w', encoding='utf-8')

    info_printer('list_make_input')
    while True:
        package_name = str(input())
        print('INPUT : {0}'.format(package_name))
        if package_name == 'END':
            break
        else:
            package_list.append(package_name)
    package_config = config_writer(package_list)
    config_descriptor.write(package_config)

    info_printer('done')
