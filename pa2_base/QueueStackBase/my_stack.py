from array_deque import ArrayDeque
from my_linked_list import LinkedList

class Stack:
    def __init__(self):
        # Pick one of these to use.
        # Stack must have the container you dont choose for Queue
        
        self.container = LinkedList()
        #self.container = ArrayDeque()

    def push(self, data):
        """Takes a parameter and adds its value onto the stack."""
        self.container.push_front(data)
    
    def pop(self):
        """Removes the item off the top of the stack and returns its value."""
        return self.container.pop_front()
    
    def get_size(self):
        """Returns the number of items currently on the stack."""
        return self.container.get_size()

    def __str__(self):
        return str(self.container)
