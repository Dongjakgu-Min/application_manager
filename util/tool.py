from adb.client import Client as AdbClient
from util.noti import err_printer, info_printer
import subprocess

# More Better Solution...?
client = AdbClient(host='127.0.0.1', port=5037)
try:
    list_device = client.devices()
except RuntimeError:
    err_printer('adb_not')
    subprocess.run(['adb', 'start-server'])
    list_device = client.devices()


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
    global client
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
    return package_name, package_path
