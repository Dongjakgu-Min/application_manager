from package.disable_package import disable_package_main
from package.package_list import show_package_list
from util.tool import check_connection, input_int, connection_is_valid
from util.error import error_printer

while True:
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

    client = check_connection()
    choice = input_int()

    if choice is 1:
        show_package_list(connection_is_valid(client))
    elif choice is 2:
        disable_package_main()
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
