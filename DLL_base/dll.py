class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev: Node = prev
        self.next: Node = next


class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

        self.curr = self.tail ## LATER curr

    def insert(self, data):
        """Inserts an item with that value in front of the node at the current position"""
        node = Node(data, self.curr.prev, self.curr)
        if self.size == 0:
            self.tail.prev = node
            self.head.next = node
        else:
            self.curr.prev.next = node
            self.curr.prev = node

        self.curr = node
        self.size += 1

        
        

    def remove(self):
        """Removes the node at the current position if there is one (otherwise does nothing)"""
        pass

    def get_value(self):
        """Returns the value of the item at the current position in the list (None if not item)"""
        if not self.curr: # LATER curr
            return None
        return self.curr.data

    def move_to_next(self):
        """Moves the current position one item closer to the tail/trailer.
        Do nothing if at end"""
        if self.curr != self.tail:
            self.curr = self.curr.next

    def move_to_prev(self):
        """Moves the current position one item closer to the head/header.
        Do nothing if at beginning"""
        if self.curr != self.tail:
            self.curr = self.curr.prev

    def move_to_pos(self, pos):
        """Moves the current position to item #position in the list"""
        pass

    def clear(self):
        """Clears all nodes from the list"""
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.curr = self.tail # LATER curr
        pass

    def get_first_node(self):
        """Returns the first Node of the list"""
        if self.size == 0:
            return None
        return self.head.next

    def get_last_node(self):
        """Returns the last Node of the list"""
        if self.size == 0:
            return None
        return self.tail.prev

    def partition(self, low, high):
        pass

    def sort(self):
        """Order the items in the list with any method that uses only your DLL structure"""
        pass

    def __len__(self):
        """Returns the number of items in the list"""
        return self.size

    def __str__(self):
        """Returns string with all the items in the list with a single space between them"""

        ## PRINT LIST FRÁ TA
        ret_str = ""
        node = self.head
        while node.next != self.tail:
            return_str += str(node.data)
            node = node.next

        return ret_str
    
    


if __name__ == "__main__":
    # create tests here if you want

    dll = DLL()

    dll.insert("A")
    print(dll.curr.data) ## "A"
    print(dll.head.next.data) ## "A"
    print(dll.tail.prev.data) ## "A"


    dll.insert("B")
    dll.insert("C")
    print()

    print(dll.curr.data) ## "C"
    print(dll.head.next.data) # "C"
    print(dll.tail.prev.data) ## "A"


    pass


