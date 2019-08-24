from util.config import config_main
from util.tool import connection_is_valid, dir_check
from package.pull_package import pull_package_by_name
from adb.client import Client as AdbClient


def disable_package_main(client):
    package_list = config_main(client)

    if package_list is not None:
        disable_package_list(client, package_list)
    elif package_list is 'Manual':
        disable_package_manual(client)
    else:
        input('\npress any key to continue...')
        return


def disable_package(device, package_name):
    valid_device = connection_is_valid(device)
    pull_package_by_name(valid_device, package_name)

    adb = valid_device.shell('pm uninstall -k --user 0 ' + package_name)
    if adb is not 'Success':
        print(adb.split('\n')[0])


def disable_package_list(device, packages):
    print('\n\nAre you sure disable this packages? '
          'Please remind package name : \n')

    for p in packages:
        print(p)

    valid_device = connection_is_valid(device)
    while True:
        check = input('\nYes(y)/No(n) : ')

        if check is 'y':
            for p in packages:
                disable_package(valid_device, p)
            print('\nDisable Complete!')
            break
        elif check is 'n':
            print('Packages are not disabled.')
            break
        else:
            print('Invalid Input!')

    input('\npress any key to continue...')


def disable_package_manual(device):
    print('Please Input Package Name : ')

