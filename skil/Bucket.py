class ItemExistsException(Exception):
    pass


class NotFoundException(Exception):
    pass


class Node:
    def __init__(self, key=None, data=None, next=None):
        self.key = key
        self.data = data
        self.next: Node = next


class Bucket:
    """Singly-linked list implementation"""

    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, key, data):
        """Adds a new key-value pair"""
        if self.contains(key):
            raise ItemExistsException()

        self.head = Node(key, data, self.head)
        self.size += 1

    def update(self, key, data):
        """Updates existing key-value pair"""
        node = self._get_node(key)
        node.data = data

    def find(self, key):
        """Returns data value for a specific key"""
        return self._get_node(key).data

    def _get_node(self, key):
        """Returns Node if found, raise NotFoundException otherwise"""
        curr = self.head
        while curr:
            if curr.key == key:
                return curr
            curr = curr.next
        raise NotFoundException()

    def contains(self, key):
        """Returns True if specific key is found in the collection, otherwise False"""
        try:
            self._get_node(key)
            return True
        except NotFoundException:
            return False

    def remove(self, key):
        """Removes the value pair with equal key from the collection"""
        temp_head = Node(next=self.head)
        prev, curr = temp_head, temp_head.next

        while curr:
            if curr.key == key:
                prev.next = curr.next
                self.head = temp_head.next
                self.size -= 1
                return
            prev, curr = curr, curr.next
        raise NotFoundException()

    def __setitem__(self, key, data):
        """Allows: some_hash_map[key] = data"""
        try:
            self.update(key, data)
        except NotFoundException:
            self.insert(key, data)

    def __getitem__(self, key):
        """Allows: my_data = some_bucket[key]"""
        return self.find(key)

    def __len__(self):
        """Allows: length_of_structure = len(some_bucket)"""
        return self.size

    # DELETE - __str__ fall er ekki í verkefnalýsingunni
    def __str__(self):
        """testing BUCKET str"""
        return_str = ""
        current = self.head
        while current:
            return_str += f"{{{current.key}:{current.data}}} "
            current = current.next
        return return_str
