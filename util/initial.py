from .noti import *
from adb.client import Client as AdbClient

import subprocess


# More Better Solution...?
client = AdbClient(host='127.0.0.1', port=5037)
try:
    list_device = client.devices()
except RuntimeError:
    err_printer('adb_not')
    subprocess.run(['adb', 'start-server'])
    list_device = client.devices()


if __name__ == "__main__":
    a = "package:/data/app/com.samsung.android.video-lzMYdKJRrqaF_wBEkgp6Yw==/base.apk=com.samsung.android.video"
    length = len(a.split(':')[-1].split('=')[-1]) + 1
    print(a[:-length])
