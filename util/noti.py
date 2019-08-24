list_error = {
    'not_connected': '[ERR] Device Not Detected. Check Device is connected or USB Debugging is ON, Waiting Connection...',
    'file_not_exist': '[ERR] file not exist! Please Check input path.',
    'not_config': '[ERR] It is not config, Did you check where is it?',
    'disconnected': '[ERR] Target Device was disconnected! Waiting Connection...',
    'adb_not': '[ERR] ADB Server not started. starting ADB Server...'}
list_info = {
    'connected': '[INFO] Device Connected!',
    'one_more_con': '[INFO] One more devices are connected. Choose Device...',
    'aapt_check': '[INFO] Check aapt already installed...',
    'aapt_ok': '[INFO] aapt already installed!',
    'aapt_not': '[INFO] aapt not installed! Installing aapt via usb debugging...',
    'aapt_complete': '[INFO] aapt install complete!',
    'config_write_info': '[INFO] if you finish writing package list, input END',
    'done': '[INFO] Done!',
    'list_make_input': '[INFO] Please input package name.\
    \n[INFO] If you want to end up append, Please input to end.\
    \n[INFO] If you want to add more package, input package name and press enter.\n'
}


def err_printer(spec):
    print(list_error[spec])


def info_printer(spec):
    print(list_info[spec])
