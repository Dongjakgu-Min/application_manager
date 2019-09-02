from util.initial import client
from util.adb.connection import *
from pathlib import Path


def adb_operation(operate):
    if operate == 'pull':
        return


def adb_pull(device, path):
    _path = Path(path)
    path_part = _path.parts
    print(path_part)
    file = Path() / path_part[-2] / path_part[-1]

    device.pull(_path.parent, './backup/' + str(file))
