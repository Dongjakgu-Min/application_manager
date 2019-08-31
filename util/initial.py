import subprocess

from .noti import *
from adb.client import Client as AdbClient
from pathlib import Path


# More Better Solution...?
client = AdbClient(host='127.0.0.1', port=5037)

if Path.is_dir(Path.cwd() / 'backup') is False:
    Path.mkdir(Path.cwd() / 'backup')

try:
    list_device = client.devices()
except RuntimeError:
    err_printer('adb_not')
    subprocess.run(['adb', 'start-server'])
    list_device = client.devices()
