from util.config import config_main
from util.adb import connection
from util.adb.adb_operate import adb_pull
from package.pull_package import pull_package_by_name


def main(client):
    package_list = config_main(client)

    if package_list is not None:
        by_list(client, package_list)
    elif package_list is 'Manual':
        manual(client)
    else:
        input('\npress any key to continue...')
        return


def execute(device, package_name):
    valid_device = connection.is_valid(device)
    adb_pull(valid_device, package_name)

    adb = valid_device.shell('pm uninstall -k --user 0 ' + package_name)
    if adb is not 'Success':
        print(adb.split('\n')[0])


def by_list(device, packages):
    print('\n\nAre you sure disable this packages? '
          'Please remind package name : \n')

    for p in packages:
        print(p)

    valid_device = connection.is_valid(device)
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


def manual(device):
    print('Please Input Package Name : ')

