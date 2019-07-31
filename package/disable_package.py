import subprocess
import sys
from config import config_main


def disable_package_main():
    package_list = config_main()

    if package_list is not None:
        disable_package_list(package_list)
    else:
        input('\npress any key to continue...')
        return


def disable_package(package_name):
    adb = subprocess.run(['adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', package_name], stdout=subprocess.PIPE, encoding='utf-8')
    if adb is not 'Success':
        print(adb.stdout.split('\n')[0])


def disable_package_list(packages):
    print('\n\nAre you sure disable this packages? Please remind package name : \n')

    for p in packages:
        print(p)

    while True:
        check = input('\nYes(y)/No(n) : ')

        if check is 'y':
            for p in packages:
                disable_package(p)
            print('\nDisable Complete!')
            break
        elif check is 'n':
            print('Packages are not disabled.')
            break
        else:
            print('Invalid Input!')
    
    input('\npress any key to continue...')


if __name__ == "__main__":
    disable_package()