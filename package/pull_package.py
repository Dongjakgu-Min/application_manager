from util.tool import dir_check
from util.adb import connection
from pathlib import Path


def pull_package_by_path(device, package_path):
    package_name = Path(package_path).parts[-2]

    valid = connection.is_valid(device)
    path = dir_check(Path.cwd() / 'backup' / package_name)

    valid.pull(package_path, path)


def pull_package_by_name(device, package_name):
    package_path = device.shell('pm path' + package_name)
    backup = dir_check(Path.cwd() / 'backup' / package_name / package_path.parts[-1])

    device.pull(package_path, backup)
