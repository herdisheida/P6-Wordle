class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = Node() # the first node ----- HELO PIAZZA
    

    def push_back(self, data):
        """Takes a parameter and adds its value to the back of the list."""
        pass

    def push_front(self, data):
        """Takes a parameter and adds its value to the front of the list."""
        pass
    

    def pop_front(self):
        """Removes the item from the front of the list and returns its value."""
        return None
        # TODO: ■ If the list is empty, return None

    def pop_back(self):
        """Removes the item from the back of the list and returns its value"""
        return None
        # TODO: ■ If the list is empty, return None


    def get_size(self):
        """Returns the number of items currently in the list."""
        return 0
    

    def __str__(self):
        """Returns a string with all the items in the list, separated by a single space."""
        return ""



# TODO: For full marks, implement all these operations (apart from __str__ and pop_back) with time complexity O(1).
