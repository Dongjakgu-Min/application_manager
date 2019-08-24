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

