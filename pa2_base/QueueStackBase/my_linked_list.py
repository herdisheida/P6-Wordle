class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None # first dude
        self.tail = None # last dude
        self.size = 0
    
    def push_back(self, data): # O(1)
        """Takes a parameter and adds its value to the back of the list."""
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def push_front(self, data): # O(1)
        """Takes a parameter and adds its value to the front of the list."""
        new_node = Node(data)
        if self.head == None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def pop_front(self): # O(1)
        """Removes the item from the front of the list and returns its value."""
        if self.head == None:
            return None
        return_data = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.size == 0:
            self.tail = None
        return return_data

    def pop_back(self):
        """Removes the item from the back of the list and returns its value."""
        current = self.head
        if current == None:
            return None
        last_node = self.tail
        if self.size == 1:
            self.tail = None
            self.head = None
            self.size -= 1
            return current.data
        while current != last_node:
            if current.next == last_node: # find next last node
                current.next = None # secondToLastNode.next = None
                self.tail = current # secondToLastNode = last_node
                self.size -= 1
                return last_node.data
            current = current.next
        

    def get_size(self): # O(1)
        """Returns the number of items currently in the list."""
        return self.size

    def __str__(self):
        """Returns a string with all the items in the list, separated by a single space."""
        return_str = ""
        current = self.head
        while current != None: # TODO: laga þettta -- get ekkki gert current.data
            return_str += f"{current.data} " # HELP TA má gera space svona
            current = current.next
        return return_str



# TODO: For full marks, implement all these operations (apart from __str__ and pop_back) with time complexity O(1).