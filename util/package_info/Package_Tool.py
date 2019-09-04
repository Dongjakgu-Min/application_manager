from util.adb.connection import check


def information(line):
    _package = line.split(':')[-1].split('=')[-1]
    _path = line[8:-(len(_package)+1)]
    _label = label(_path)

    return {'package': _package, 'label': _label if len(_label) is not 0 else None, 'path': _path}


def label(path):
    device = check()
    name = device.shell('/data/local/tmp/aapt d badging ' +
                        path + ' | grep application-label-ko:')
    return name.split(':')[-1].strip()
