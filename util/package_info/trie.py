class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, item):
        curr_node = self.head

        for elem in item:
            if elem not in curr_node.children:
                curr_node.children[elem] = Node(elem)
            curr_node = curr_node.children[elem]

        curr_node.data = item

    def insert_package(self, items):
        _list = list()

        for i in items:
            self.insert(i['package'])
            _list.append(i['package'])

        return _list

    def search(self, item):
        curr_node = self.head

        for elem in item:
            if elem in item.children:
                curr_node = curr_node.children[elem]
            else:
                return False

        if curr_node.data is not None:
            return True

    def starts_with(self, prefix):
        curr_node = self.head
        result = list()
        sub_trie = None

        for elem in prefix:
            if elem in curr_node.children:
                curr_node = curr_node.children[elem]
                sub_trie = curr_node
            else:
                return None

        queue = list(sub_trie.children.values())

        while queue:
            curr = queue.pop()
            if curr.data is not None:
                result.append(curr.data)

            queue += list(curr.children.values())

        return result

    def print_start_with(self, prefix):
        _result = self.starts_with(prefix)

        if isinstance(_result, type(None)):
            print('[INFO] No match item')
            return

        for i in _result:
            print("{0} ".format(i), end='', flush=True)


class PackageList:
    def __init__(self, package_list):
        self.label = Trie()
        self.package = Trie()
        self.package_mode = False

        self.label.insert(package_list['label'])
        self.package.insert(package_list['package'])

    def change_mode(self):
        print('[INFO] Change input mode : {0}'.format('package' if self.package_mode is True else 'label'))
        self.package_mode = True

    def find_by_label(self, prefix):
        label_result = self.label.starts_with(prefix)

        if isinstance(label_result, type(None)):
            print('[INFO] No match item')
            return

        for i in label_result:
            print("{0} ".format(i), end='', flush=True)

    def find_by_package(self, prefix):
        package_result = self.label.starts_with(prefix)

        if isinstance(package_result, type(None)):
            print('[INFO] No match item')
            return

        for i in package_result:
            print("{0} ".format(i), end='', flush=True)

    def find(self, prefix):
        if self.package_mode is True:
            _result = self.package.starts_with(prefix)
        else:
            _result = self.label.starts_with(prefix)

        if isinstance(_result, type(None)):
            print('[INFO] No match item')
            return

        return _result

    def is_exist_label(self, prefix):
        self.label.starts_with(prefix)

    def is_exist_package(self, prefix):
        self.package.starts_with(prefix)

