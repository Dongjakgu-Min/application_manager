from util.config import config_main
from util.adb import connection
from util.adb.adb_operate import adb_pull
from util.package_info.Package import PackageList
from util.noti import info_printer
from util.tool import write_list
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

    for i in package_name:
        adb_pull(valid_device, i['path'])

        adb = valid_device.shell('pm uninstall -k --user 0 ' + i['package'])
        print(adb)
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
    print(_list)

    packages = PackageList(_list)
    result = write_list(packages)
    execute(client, result)

    info_printer('package_manual_end')
