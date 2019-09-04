from util.initial import client
from util.noti import err_printer, info_printer
from util.tool import input_int


def check():
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


def is_valid(user):
    connected_list = []

    for i in client.devices():
        connected_list.append(i.serial)

    if user.serial not in connected_list:
        err_printer('disconnected')

        while user not in client.devices():
            pass
        info_printer('connected')
    return user
