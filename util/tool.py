from adb.client import Client as AdbClient
from .noti import err_printer, info_printer
from .initial import client
from pathlib import Path
import subprocess


def check_connection():
    list_device = client.devices()

    if len(list_device) is 0:
        err_printer('not_connected')

        while len(client.devices()) is 0:
            pass
        info_printer('connected')
        list_device = client.devices()

    if len(list_device) > 1:
        info_printer('one_more_con')
        for i, d in enumerate(list_device):
            print('{0}. {1}'.format(i, d.serial))
        i = input_int()
        return list_device[i]

    return list_device[0]


def connection_is_valid(user):
    connected_list = []

    for i in client.devices():
        connected_list.append(i.serial)

    if user.serial not in connected_list:
        err_printer('disconnected')

        while user not in client.devices():
            pass
        info_printer('connected')
    return user


def input_int():
    try:
        choice = int(input('input number what you want to do : '))
    except ValueError:
        choice = None
    return choice


def get_package_information(line):
    package_name = line.split(':')[-1].split('=')[-1]
    package_path = line[8:-(len(package_name)+1)]
    print(package_path)
    package_label = get_package_label(package_path)
    return package_name, package_label


def config_writer(data):
    result = '\n'.join(data)
    return result


def get_package_label(path):
    device = check_connection()
    name = device.shell('/data/local/tmp/aapt d badging ' +
                        path + ' | grep application-label-ko:')
    return name.split(':')[-1].strip()


def check_aapt(device):
    info_printer('aapt_check')
    result = device.shell('/data/local/tmp/aapt')

    if 'not found' in result:
        info_printer('aapt_not')
        device.push('./util/aapt/aapt', '/data/local/tmp/aapt', 0o755)
        info_printer('aapt_complete')
    else:
        info_printer('aapt_ok')


def delete_aapt():
    device = check_connection()
    device.shell('rm /data/local/tmp/aapt')


def dir_check(path):
    parent_dir = Path(path).parent

    if parent_dir.is_dir() is False:
        Path.mkdir(parent_dir)

    return path


def file_check(path):
    if not Path(path).exists:
        error_printer('file_not_exist')
        return False
    if not Path(path).is_dir:
        error_printer('not_config')
        return False

    return True
