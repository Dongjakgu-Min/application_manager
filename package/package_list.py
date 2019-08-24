from adb.client import Client as AdbClient
from util.tool import *
from util.noti import *
from util.trie import Trie
from pathlib import Path
from keyboard import is_pressed


def show_package_list(device):
    valid_device = connection_is_valid(device)
    check_aapt(valid_device)
    a = valid_device.shell('pm list packages -s -f')

    for line in a.split('\n'):
        if len(line) is not 0:
            package_name, package_label, _ = get_package_information(line)
            if len(package_label) is 0:
                print('Package Name : {0}'.format(package_name))
            else:
                print('Package Name : {0}, Package Label : {1}'.format(
                    package_name, package_label))

    input('\npress any key to continue...')


def get_package_list(device):
    valid_device = connection_is_valid(device)
    check_aapt(valid_device)
    a = valid_device.shell('pm list packages -s -f')
    package_list = list()

    for line in a.split('\n'):
        if len(line) is not 0:
            package = dict()
            package['package'], package_label, package['path'] = get_package_information(line)
            if len(package_label) is not 0:
                package['label'] = package_label
            package_list.append(package)

    return package_list


def show_package_by_name(device):
    name = input('Input Package Name : ')
    result = []

    valid_device = connection_is_valid(device)

    for p in print_package_list(valid_device):
        if name in p:
            print(p)

    input('\npress any key to continue...')


def print_package_list(device):
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

    for p in print_package_list(valid_device):
        if name in p:
            result.append(p)
    return result


def make_package_list(device):
    valid_device = connection_is_valid(device)
    # show_package_list(valid_device)
    package_list = get_package_list(valid_device)
    packages = list()

    info_printer('config_write_info')
    config_name = str(input('Please Input config file name : '))

    config_descriptor = Path(Path.cwd() / 'config' /
                             config_name).open('w', encoding='utf-8')

    helper = Trie()
    package_item = helper.insert_package(package_list)

    info_printer('list_make_input')
    while True:
        package_input = str(input('> '))
        if package_input == 'END':
            break
        elif package_input not in package_item:
            print(helper.print_start_with(package_input))
        else:
            packages.append(package_input)
    package_config = config_writer(packages)
    config_descriptor.write(package_config)

    info_printer('done')
