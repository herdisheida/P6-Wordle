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

    def __init__(self, node: Node=None):
        self.head = None
        self.size = 0

        self.head = node # DELETE LATER

    def insert(self, key, data):
        """ Adds this value pair to the collection """
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
        """ Sets the data value of the value pair with equal key to data """
        node = self._get_node(key)
        node.data = data

    def find(self, key):
        """ Returns the data value of the value pair with equal key
         
          klsdfajklsadjfkjasjl """
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
        """ Override to allow this syntax: some_hash_map[key] = data """
        try:
            self.update(key, data)
        except NotFoundException:
            self.insert(key, data)

    def __getitem__(self, key):
        """ Override to allow this syntax: my_data = some_bucket[key] """
        return self.find(key)

    def __len__(self):
        """ Override to allow this syntax: length_of_structure = len(some_bucket) """
        return self.size
    

    # DELETE - __str__ fall er ekki í verkefnalýsingunni
    def __str__(self):
        """ testing BUCKET str """
        return_str = ""
        current = self.head
        while current:
            return_str += f"{{{current.key}:{current.data}}} "
            current = current.next
        return return_str




# TODO -- muna að búa til hash fall :D :D :D
# TODO -- reyna gera fall fyrir að finna index -- alltaf sami hluturinn
class HashMap:

    def __init__(self):

        self.item_count = 0 # num of items in the entire data structure
        self.lis_size = 8 # # num of buckets

        self.bucket_list = [Bucket() for _ in range(self.lis_size)]
        # self.bucket_list = [None for _ in range(self.lis_size)]

        

        # self.lis_size = 4
        # self.item_count = 4
        # self.bucket_list = [Bucket(Node(1, "einn", Node(2, "tveir"))), Bucket(Node(3, "þrír", Node(4, "fjórir"))), Bucket(), Bucket(Node(10, "tía", Node(14, "fjórri")))]


    def insert(self, key, data):
        """ Adds this value pair to the collection """
        index = hash(key) % self.lis_size
        self.bucket_list[index].insert(key, data)


    def update(self, key, data):
        """ Sets the data value of the value pair with equal key to data """
        index = hash(key) % self.lis_size
        self.bucket_list[index].update(key, data)

    def find(self, key):
        """ Returns the data value of the value pair with equal key """
        index = hash(key) % self.lis_size
        return self.bucket_list[index].find(key)

    def contains(self, key):
        """ Returns True if equal key is found in the collection, otherwise False """
        index = hash(key) % self.lis_size
        return self.bucket_list[index].contains(key)
    
    def remove(self, key):
        """ Removes the value pair with equal key from the collection """
        index = hash(key) % self.lis_size
        self.bucket_list[index].remove(key)
    
    def __setitem__(self, key, data):
        """ Override to allow this syntax: some_hash_map[key] = data """
        index = hash(key) % self.lis_size
        self.bucket_list[index][key] = data # ... questinable

    def __getitem__(self, key):
        """ Override to allow this syntax: my_data = some_hash_map[key """
        index = hash(key) % self.lis_size
        return self.bucket_list[index][key] # ... questinable

    def __len__(self):
        """ Returns the number of items in the entire data structure """
        return self.item_count
    
    def rebuild(self):
        """ When the number of items in the HashMap has reached 120% of the number of buckets
         (length of array or list), it must doubling the number of buckets """
        if self.lis_size * 1.2 >= self.item_count:

            # initalize bucket list
            temp = self.bucket_list
            self.lis_size *= 2
            self.bucket_list = [Bucket() for _ in range(self.lis_size)]
            
            # re allocate items
            for x in range(self.lis_size):
                bucket = temp[x]
                curr= bucket
                while curr:
                    index = hash(curr.key) % self.lis_size
                    self.bucket_list[index].insert(curr.key, curr.data)

                
                pass # TODO



    def __str__(self):
        """ testing HASH MAP str """
    # DELETE later - þessi klasi hefur ekki __str__ func
        ret = ""
        for x in self.bucket_list:
            ret += str(x)
        return ret


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