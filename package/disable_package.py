from util.config import config_main
from util.adb import connection
from util.adb.adb_operate import adb_pull
from util.package_info.trie import PackageList
from util.noti import info_printer

from package import package_list


def main(client):
    package_list_ = config_main(client)

    if package_list_ is None:
        return
    elif package_list_ == 'Manual':
        manual(client)
    else:
        by_list(client, package_list_)


def execute(device, package_name):
    valid_device = connection.is_valid(device)
    adb_pull(valid_device, package_name)

    adb = valid_device.shell('pm uninstall -k --user 0 ' + package_name)
    if adb is not 'Success':
        print(adb.split('\n')[0])


def by_list(device, packages):
    valid_device = connection.is_valid(device)

    print('\n\nAre you sure disable this packages? '
          'Please remind package name : \n')

    for p in packages:
        print(p)

    while True:
        check = input('\nYes(y)/No(n) : ')

        if check is 'y':
            for p in packages:
                execute(valid_device, p)
            print('\nDisable Complete!')
            break
        elif check is 'n':
            print('Packages are not disabled.')
            break
        else:
            print('Invalid Input!')

    input('\npress any key to continue...')


def manual(client):
    valid_device = connection.is_valid(client)
    _list = package_list.get(valid_device)

    packages = PackageList(_list)

    while True:
        _str = input('\n> ')

        if _str == '/END':
            break
        elif _str == '/MODE':
            packages.change_mode()

        if len(_str) is 0:
            continue

        items = packages.find(_str)
        print(items)
        if len(items) is 1:
            execute(valid_device, items[0])
        else:
            for i in items:
                print("{0} ".format(i), end='', flush=True)

    info_printer('package_manual_end')
