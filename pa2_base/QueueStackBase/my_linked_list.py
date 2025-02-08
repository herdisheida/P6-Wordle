class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None # first node
        self.tail = None # last node
        self.size = 0    # num of nodes
    
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
            self.tail = self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def pop_front(self): # O(1)
        """Removes the item from the front of the list and returns its value."""
        if self.head == None:
            return None
          
        first_node = self.head
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.head = first_node.next
        self.size -= 1
        return first_node.data


    def pop_back(self):
        """Removes the item from the back of the list and returns its value."""
        if self.head == None:
            return None
        
        last_node = self.tail
        if self.size == 1:
            self.head = self.tail = None
        else:
            # find the second-to-last-node (thnew tail)
            current = self.head
            while current.next != last_node:
                current = current.next
            current.next = None # disconnect the new tail from the old tail
            self.tail = current # second-to-last-node becomes the new tail
        self.size -= 1
        return last_node.data
        

    def get_size(self): # O(1)
        """Returns the number of items currently in the list."""
        return self.size


    def __str__(self):
        """Returns a string with all the items in the list, separated by a single space."""
        return_str = ""
        current = self.head
        while current != None:
            if current != self.tail:
                return_str += f"{current.data} "
            else:
                return_str += f"{current.data}"
            current = current.next
        return return_str

        # return_str = ""
        # current = self.head
        # while current != None: # TODO: laga þettta -- get ekkki gert current.data -- UGLY...
        #     return_str += f"{current.data} " # HELP TA má gera space svona
        #     current = current.next
        # return return_str