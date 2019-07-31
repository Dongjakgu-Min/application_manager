from package.disable_package import disable_package_main
from package.package_list import show_package_list

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
    print('5: exit')

    print('\n')

    try:
        choice = int(input('input number what you want to do : ')) 
    except ValueError:
        choice = None

    if choice is 1:
        show_package_list()
    elif choice is 2:
        disable_package_main()
    elif choice is 3:
        print('Not implemented')
    elif choice is 4:
        print('Not implemented')
    elif choice is 5:
        exit(0)
    else:
        print('Invalid Input!')