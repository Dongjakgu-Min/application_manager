from util.aapt.aapt_handler import check_aapt
from util.adb.connection import is_valid
from util.package_info.get_package import information
from util.tool import *
from util.noti import *
from util.package_info.trie import PackageList
from pathlib import Path


def show_package_list(device):
    valid_device = is_valid(device)
    check_aapt(valid_device)
    a = valid_device.shell('pm list packages -s -f')

    for line in a.split('\n'):
        if len(line) is not 0:
            package_name, package_label, _ = information(line)
            if len(package_label) is 0:
                print('Package Name : {0}'.format(package_name))
            else:
                print('Package Name : {0}, Package Label : {1}'.format(
                    package_name, package_label))

    input('\npress any key to continue...')


def get_package_list(device):
    valid_device = is_valid(device)
    check_aapt(valid_device)
    a = valid_device.shell('pm list packages -s -f')
    package_list = list()

    for line in a.split('\n'):
        if len(line) is not 0:
            package = dict()
            package['package'], package_label, package['path'] = information(line)
            if len(package_label) is not 0:
                package['label'] = package_label
            package_list.append(package)

    return package_list


def show_package_by_name(device):
    name = input('Input Package Name : ')
    result = []

    valid_device = is_valid(device)

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

    valid_device = is_valid(device)

    for p in print_package_list(valid_device):
        if name in p:
            result.append(p)
    return result


def make_package_list(device):
    valid_device = is_valid(device)
    # show_package_list(valid_device)
    package_list = get_package_list(valid_device)
    packages = list()

    info_printer('config_write_info')
    config_name = str(input('Please Input config file name : '))

    config_descriptor = Path(Path.cwd() / 'config' /
                             config_name).open('w', encoding='utf-8')

    helper = PackageList(package_list)

    info_printer('list_make_input')
    while True:
        package_input = str(input('> '))
        if package_input == '/END':
            break
        elif package_list == '/mode':
            helper.change_mode()
        else:
            packages.append(package_input)
    package_config = config_writer(packages)
    config_descriptor.write(package_config)

    info_printer('done')
