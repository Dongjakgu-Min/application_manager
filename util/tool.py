from adb.client import Client as AdbClient
from util.error import list_error, list_info
import subprocess

# More Better Solution...?
client = AdbClient(host='127.0.0.1', port=5037)
try:
    device = client.devices()
except RuntimeError:
    subprocess.run(['adb', 'start-server'])
    device = client.devices()


def check_connection():
    global device

    if len(device) is 0:
        print(list_error['not_connected'])

        while len(client.devices()) is 0:
            pass
        print(list_info['connected'])
    if len(device) > 1:
        print(list_info['one_more_con'])
        for i, d in enumerate(device):
            print('{0}. {1}'.format(i, d.serial))
        i = input_int()
        return device[i]

    return device[0]


def connection_is_valid(user):
    global device, client

    connected = client.devices()
    print(connected)

    if user not in connected:
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
