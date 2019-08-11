from util.config import config_main
from util.tool import connection_is_valid, check_connection
from adb.client import Client as AdbClient


def disable_package_main(client):
    package_list = config_main(client)

    if package_list is not None:
        disable_package_list(package_list, client)
    else:
        input('\npress any key to continue...')
        return


def disable_package(package_name, client):
    adb = client.shell('pm uninstall -k --user 0 ' + package_name)
    if adb is not 'Success':
        print(adb.split('\n')[0])


def disable_package_list(packages, client):
    print('\n\nAre you sure disable this packages? '
          'Please remind package name : \n')

    for p in packages:
        print(p)

    valid_device = connection_is_valid(client)
    while True:
        check = input('\nYes(y)/No(n) : ')

        if check is 'y':
            for p in packages:
                disable_package(p, valid_device)
            print('\nDisable Complete!')
            break
        elif check is 'n':
            print('Packages are not disabled.')
            break
        else:
            print('Invalid Input!')

    input('\npress any key to continue...')
