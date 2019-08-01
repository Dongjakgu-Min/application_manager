from adb.client import Client as AdbClient


list_error = {
    'not_connected': '[ERR] Device Not Detected. Check Device is connected or USB Debugging is ON, Waiting Connection...'}
list_info = {
    'connected': '[INFO] Device Connected!'
}


def check_connection():
    client = AdbClient(host='127.0.0.1', port=5037)
    device = client.devices()

    if len(device) is 0:
        print(list_error['not_connected'])

        while len(client.devices()) is 0:
            pass
        print(list_info['connected'])
