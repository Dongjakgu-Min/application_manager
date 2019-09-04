class Node(object):
    def __init__(self, key, package, data=None):
        self.key = key
        self.package = package
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self, key):
        self.head = Node(None, None)
        self.key = key

    def insert(self, item):
        curr_node = self.head

        for elem in item[self.key]:
            if elem not in curr_node.children:
                curr_node.children[elem] = Node(elem, item)
            curr_node = curr_node.children[elem]

        curr_node.data = item[self.key]

    def search(self, item):
        curr_node = self.head

        for elem in item:
            if elem in curr_node.children:
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

        if len(queue) is 0 and sub_trie.data == prefix:
            result.append(sub_trie.package)

        while queue:
            curr = queue.pop()
            if curr.data is not None:
                result.append(curr.package)

            queue += list(curr.children.values())
        print(result)

        return result
