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
        # find first node
        # make new_node.next = first_node
        # make self.head = new_node
        pass
        self.size += 1

    def pop_front(self): # O(1)
        """Removes the item from the front of the list and returns its value."""
        if self.head.data == None:
            return None

        # make self.head = self.head.next
        # the old self.head should be returned
        # TODO: ■ If the list is empty, return None

    def pop_back(self):
        """Removes the item from the back of the list and returns its value"""
        # find last node
        # return last_node
        # find next_last_node --- next_last_node.next = None
        return None
        # TODO: ■ If the list is empty, return None


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