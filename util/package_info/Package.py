from util.package_info.Trie import Trie


class PackageList:
    def __init__(self, package_list):
        self.package = Trie('package')
        self.label = Trie('label')
        self.package_mode = True

        for i in package_list:
            self.package.insert(i)

    def change_mode(self):
        print('[INFO] Change input mode : {0}'
              .format('package' if self.package_mode is True else 'label'))
        self.package_mode = not self.package_mode

    def is_package_mode(self):
        return self.package_mode

    def get_mode(self):
        return 'package' if self.package_mode is True else 'label'

    def find(self, prefix):
        if self.package_mode is True:
            _result = self.package.starts_with(prefix)
        else:
            _result = self.label.starts_with(prefix)
        if isinstance(_result, type(None)):
            print('[INFO] No match item')
            return list()

        return _result
