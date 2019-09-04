from util.initial import client
from util.adb.connection import *
from pathlib import Path


def adb_operation(operate):
    if operate == 'pull':
        return


def adb_pull(device, path):
    _path = Path(path)
    path_part = _path.parts
    file = Path().cwd() / 'backup' / path_part[-2]

    device.pull(str(_path.parent), str(file))
