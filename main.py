from package import disable_package, package_list
from util.tool import input_int
from util.adb import connection

while True:
    client = connection.check()

    print('\n')
    print('/////////////////////////////////////////////////////////')
    print('/                                                       /')
    print('/                 Application Manager                   /')
    print('/                                                       /')
    print('/                                                       /')
    print('/          DongjakGuMin(songyw9812@gmail.com)           /')
    print('/                                                       /')
    print('/////////////////////////////////////////////////////////')
    print('\n')

    print('1: show package list')
    print('2: disable package list')
    print('3: pull package')
    print('4: push package')
    print('5: miscellaneous')
    print('6: exit')

    print('\n')
    choice = input_int()

    if choice is 1:
        package_list.show(connection.is_valid(client))
    elif choice is 2:
        disable_package.main(connection.is_valid(client))
    elif choice is 3:
        print('Not implemented')
    elif choice is 4:
        print('Not implemented')
    elif choice is 5:
        print('Not implemented')
    elif choice is 6:
        exit(0)
    else:
        print('Invalid Input!')
