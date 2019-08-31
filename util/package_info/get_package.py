from util.adb.connection import check


def information(line):
    package_name = line.split(':')[-1].split('=')[-1]
    package_path = line[8:-(len(package_name)+1)]
    package_label = label(package_path)
    return package_name, package_label, package_path


def label(path):
    device = check()
    name = device.shell('/data/local/tmp/aapt d badging ' +
                        path + ' | grep application-label-ko:')
    return name.split(':')[-1].strip()
