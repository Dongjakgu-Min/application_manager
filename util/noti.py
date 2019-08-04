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
    'aapt_installed': '[INFO] aapt install complete!'
}


def err_printer(spec):
    print(list_error[spec])


def info_printer(spec):
    print(list_info[spec])
