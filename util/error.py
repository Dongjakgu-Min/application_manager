list_error = {
    'not_connected': '[ERR] Device Not Detected. Check Device is connected or USB Debugging is ON, Waiting Connection...',
    'file_not_exist': '[ERR] file not exist! Please Check input path.',
    'not_config': '[ERR] It is not config, Did you check where is it?',
    'disconnected': '[ERR] Target Device was disconnected! Waiting Connection...'}
list_info = {
    'connected': '[INFO] Device Connected!',
    'one_more_con': '[INFO] One more devices are connected. Choose Device...'
}


def error_printer(spec):
    print(list_error[spec])
