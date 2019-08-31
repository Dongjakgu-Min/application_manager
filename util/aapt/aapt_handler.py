from util.noti import info_printer
from util.adb.connection import check


def check_aapt(device):
    info_printer('aapt_check')
    result = device.shell('/data/local/tmp/aapt')

    if 'not found' in result:
        info_printer('aapt_not')
        device.push('./util/aapt/aapt', '/data/local/tmp/aapt', 0o755)
        info_printer('aapt_complete')
    else:
        info_printer('aapt_ok')


def delete_aapt():
    device = check()
    device.shell('rm /data/local/tmp/aapt')

