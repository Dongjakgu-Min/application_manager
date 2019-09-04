from util.aapt.aapt_handler import check_aapt
from util.adb import connection
from util.package_info import Package_Tool, Package
from util.noti import *
from util.tool import write_list
from pathlib import Path
from tqdm import tqdm

import json


def show(device):
    valid_device = connection.is_valid(device)
    check_aapt(valid_device)
    a = valid_device.shell('pm list packages -s -f')

    for line in a.split('\n'):
        if len(line) is not 0:
            item = Package_Tool.information(line)
            if len(item['label']) is 0:
                print('Package Name : {0}'.format(item['package']))
            else:
                print('Package Name : {0}, Package Label : {1}'.format(
                    item['package'], item['label']))

    input('\npress any key to continue...')


def get(device):
    valid_device = connection.is_valid(device)
    check_aapt(valid_device)

    info_printer('package_list_loading')
    a = valid_device.shell('pm list packages -s -f')
    package_list = list()

    for line in tqdm(a.split('\n')):
        if len(line) is not 0:
            package_list.append(Package_Tool.information(line))

    return package_list


def show_by_name(device):
    name = input('Input Package Name : ')

    valid_device = connection.is_valid(device)

    for p in get_list(valid_device):
        if name in p:
            print(p)

    input('\npress any key to continue...')


def get_list(device):
    adb = device.shell('pm list packages -s')
    result = []

    for line in adb.split('\n'):
        if len(line) is not 0:
            result.append(line.split(':')[-1].split('=')[-1])

    return result


def find_package_by_name(device):
    name = input('Input Package Name : ')
    result = []

    valid_device = connection.is_valid(device)

    for p in get_list(valid_device):
        if name in p:
            result.append(p)

    return result


def make(device):
    valid_device = connection.is_valid(device)
    package_list = get(valid_device)

    info_printer('config_write_info')
    config_name = str(input('Please Input config file name : ')) + '.json'

    config_descriptor = Path(Path.cwd() / 'config' /
                             config_name).open('w', encoding='utf-8')

    helper = Package.PackageList(package_list)

    info_printer('list_make_input')
    packages = write_list(helper)

    # package_config = config_writer(packages)
    print(packages)
    print(json.dumps(packages))
    config_descriptor.write(json.dumps(packages))
    config_descriptor.close()

    info_printer('done')


def load():
    config = Path.open()
