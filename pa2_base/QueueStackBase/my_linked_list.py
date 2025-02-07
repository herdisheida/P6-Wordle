class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = Node() # the first node ----- HELO PIAZZA
        self.head = Node(10)

        self.size = 0
    
    def push_back(self, data): # O(1)
        """Takes a parameter and adds its value to the back of the list."""
        pass
        self.size += 1

    def push_front(self, data): # O(1)
        """Takes a parameter and adds its value to the front of the list."""
        pass
        self.size += 1


    def pop_front(self): # O(1)
        """Removes the item from the front of the list and returns its value."""
        return None
        # TODO: ■ If the list is empty, return None

    def pop_back(self):
        """Removes the item from the back of the list and returns its value"""
        return None
        # TODO: ■ If the list is empty, return None


    def get_size(self): # O(1)
        """Returns the number of items currently in the list."""
        return self.size

    def __str__(self):
        """Returns a string with all the items in the list, separated by a single space."""
        return_str = ""
        current = self.head
        while current.data != None:
            return_str += f"{current.data} " # HELP TA má gera space svona
            current = current.next
        return return_str



# TODO: For full marks, implement all these operations (apart from __str__ and pop_back) with time complexity O(1).