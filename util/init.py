from util.noti import err_printer, info_printer
from util.tool import get_device
from adb.client import Client as AdbClient


def check_aapt():
    device = get_device()
    info_printer('aapt_check')
    result = device.shell('/data/local/tmp/aapt')

    if 'not found' in result:
        info_printer('aapt_not')
        device.push('./util/aapt/aapt', '/data/local/tmp/aapt', 0o755)
        info_printer('complete')
    else:
        info_printer('aapt_ok')


def get_package_label(path):
    device = get_device()
    name = device.shell('/data/local/tmp/aapt d badging ' +
                        path + ' | grep application-label-ko:')
    return name.split(':')[-1].strip()