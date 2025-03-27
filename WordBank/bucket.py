class NotFoundException(Exception):
    pass

class ItemExistsException(Exception):
    pass

class Node:
    def __init__(self, key, data, next = None):
        self.key = key
        self.data = data
        self.next = next

class Bucket:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def _find_node(self, key):
        node = self.head
        while node != None:
            if node.key == key:
                return node
            node = node.next
        raise NotFoundException()

    def insert(self, key, data):
        try:
            self._find_node(key)
            raise ItemExistsException()
        except NotFoundException:
            pass
        except:
            raise
        self.head = Node(key, data, self.head)
        self.size += 1

    def update(self, key, data):
        self._find_node(key).data = data

    def find(self, key):
        return self._find_node(key).data

    def contains(self, key):
        try:
            self._find_node(key)
            return True
        except NotFoundException:
            return False

    def _remove(self, key, node):
        if node == None:
            raise NotFoundException()
        if node.key == key:
            return node.next
        node.next = self._remove(key, node.next)
        return node

    def remove(self, key):
        self.head = self._remove(key, self.head)
        self.size -= 1

    def __setitem__(self, key, data):
        try:
            self.update(key, data)
        except NotFoundException:
            self.insert(key, data)
    
    def __getitem__(self, key):
        return self.find(key)

    def __len__(self):
        return self.size

    def pop_next(self):
        if self.head == None:
            return None
        key = self.head.key
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return key, data

    def __str__(self):
        ret_str = ""
        node = self.head
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str