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
    """Implement the class Bucket with a singly-linked list"""

    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, key, data):
        """Adds this value pair to the collection"""
        if self.contains(key):
            raise ItemExistsException()

        new_node = Node(key, data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def update(self, key, data):
        """Sets the data value of the value pair with equal key to data"""
        node = self._get_node(key)
        node.data = data

    def find(self, key):
        """Returns the data value of the value pair with equal key"""
        return self._get_node(key).data

    def _get_node(self, key):
        curr = self.head
        while curr:
            if curr.key == key:
                return curr
            curr = curr.next
        raise NotFoundException()

    def contains(self, key):
        """Returns True if equal key is found in the collection, otherwise False"""
        try:
            self._get_node(key)
            return True
        except NotFoundException:
            return False

    def remove(self, key):
        """Removes the value pair with equal key from the collection"""
        if self.head == None:
            raise NotFoundException()

        if self.head.key == key:
            self.head = self.head.next
            self.size -= 1
            return

        curr = self.head
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                self.size -= 1
                return
            curr = curr.next
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
