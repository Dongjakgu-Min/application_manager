from adb.client import Client as AdbClient
from util.error import list_error, list_info
import subprocess

# More Better Solution...?
client = AdbClient(host='127.0.0.1', port=5037)
try:
    list_device = client.devices()
except RuntimeError:
    subprocess.run(['adb', 'start-server'])
    list_device = client.devices()
device = None


def check_connection():
    global list_device

    if len(list_device) is 0:
        print(list_error['not_connected'])

        while len(client.devices()) is 0:
            pass
        print(list_info['connected'])
    if len(list_device) > 1:
        print(list_info['one_more_con'])
        for i, d in enumerate(list_device):
            print('{0}. {1}'.format(i, d.serial))
        i = input_int()
        return set_device(list_device[i])

    return set_device(list_device[0])


def connection_is_valid(user):
    global client
    connected_list = []

    for i in client.devices():
        connected_list.append(i.serial)

    if user.serial not in connected_list:
        print(list_error['disconnected'])

        while user not in client.devices():
            pass
        print(list_info['connected'])
    return user


def input_int():
    try:
        choice = int(input('input number what you want to do : '))
    except ValueError:
        choice = None
    return choice


def set_device(_device):
    global device
    device = _device
    return _device


def get_device():
    global device
    return device
