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
    """ Implement the class Bucket with a singly-linked list """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

        # self.head = Node(1, "A")
        # self.head.next = Node(2, "B")
        # self.head.next.next = Node(3, "C")
        # self.tail = self.head.next.next 


    def insert(self, key, data):
        """ Adds this value pair to the collection """
        if self.contains(key):
            raise ItemExistsException()

        new_node = Node(key, data)
        if self.head == None:
            self.tail = self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def update(self, key, data):
        """ Sets the data value of the value pair with equal key to data """
        node = self._get_node(key)
        node.data = data

    def find(self, key):
        """ Returns the data value of the value pair with equal key """
        return self._get_node(key).data
            
    def _get_node(self, key):
        curr = self.head
        while curr:
            if curr.key == key:
                return curr
            curr = curr.next
        raise NotFoundException()
        
    def contains(self, key):
        """ Returns True if equal key is found in the collection, otherwise False """
        try:
            self._get_node(key)
            return True
        except NotFoundException:
            return False

    def remove(self, key):
        """ Removes the value pair with equal key from the collection """
        curr = self.head
        while curr.next != None:

            if curr.next.key == key: # key found
                del_node = curr.next
                curr.next = curr.next.next
                self.size -= 1
                return del_node
            curr = curr.next
        raise NotFoundException()

    def __setitem__(self, key, data):
        """ Override to allow this syntax: some_hash_map[key] = data """
        pass

    def __getitem__(self, key):
        """ Override to allow this syntax: my_data = some_bucket[key] """
        pass

    def __len__(self):
        """ Override to allow this syntax: length_of_structure = len(some_bucket) """
        return self.size
    

    # DELETE - __str__ fall er ekki í verkefnalýsingunni
    def __str__(self):  # O(n)
        """Returns a string with all the items in the list, separated by a single space."""
        return_str = ""
        current = self.head
        while current:
            return_str += f"{{{current.key}:{current.data}}} "
            current = current.next
        return return_str


class HashMap:

    def _init(self):
        self.size = 0
        self.bucket_list = [Bucket() for _ in range(self.lis_size)]


    def insert(self, key, data):
        """ Adds this value pair to the collection """
        pass

    def update(self, key, data):
        """ Sets the data value of the value pair with equal key to data """
        pass

    def find(self, key):
        """ Returns the data value of the value pair with equal key """
        pass

    def contains(self, key):
        """ Returns True if equal key is found in the collection, otherwise False """
        pass

    def remove(self, key):
        """ Removes the value pair with equal key from the collection """
        pass

    def __setitem__(self, key, data):
        """ Override to allow this syntax: some_hash_map[key] = data """
        pass

    def __getitem__(self, key):
        """ Override to allow this syntax: my_data = some_hash_map[key """
        pass

    def __len__(self):
        """ Override to allow this syntax: length_of_structure = len(some_hash_map) """
        pass

class MyHashableKey:

    def __init__(self, int_value, str_value):
        """ A constructor that takes an integer value and a string value """
        self.int_value = int_value
        self.str_value = str_value

    def __eq__(self, other): # TA - questionable...
        """ Compares two instances of MyHashableKey and returns True if their values are equal, otherwise False """
        return (self.int_value, self.str_value) == (other.int_value, other.str_value)

    def __hash__(self):
        """ Returns a positive integer """
        pass