from util.noti import err_printer, info_printer
from util.tool import check_connection
from adb.client import Client as AdbClient


def check_aapt():
    device = check_connection()
    info_printer('aapt_check')
    result = device.shell('/data/local/tmp/aapt')

    if 'not found' in result:
        info_printer('aapt_not')
        device.push('./util/aapt/aapt', '/data/local/tmp/aapt', 0o755)
        info_printer('complete')
    else:
        info_printer('aapt_ok')


def get_package_label(path):
    device = check_connection()
    name = device.shell('/data/local/tmp/aapt d badging ' +
                        path + ' | grep application-label-ko:')
    return name.split(':')[-1].strip()


if __name__ == "__main__":
    a = "package:/data/app/com.samsung.android.video-lzMYdKJRrqaF_wBEkgp6Yw==/base.apk=com.samsung.android.video"
    length = len(a.split(':')[-1].split('=')[-1]) + 1
    print(a[:-length])    
