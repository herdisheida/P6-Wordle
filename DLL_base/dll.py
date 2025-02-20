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

        self.current_pos = self.tail

    def insert(self, data):
        """Inserts an item with that value in front of the node at the current position"""
        node = Node(data, self.current_pos.prev, self.current_pos)
        self.current_pos.prev.next = node # connect left to newNode (left->new)
        self.current_pos.prev = node # connect right to newNode (new<-right)
        self.current_pos = node
        self.size += 1

        
    def remove(self):
        """Removes the node at the current position if there is one (otherwise does nothing)"""
        if self.current_pos != self.tail: # and self.current_pos is not None:
            self.current_pos.prev.next = self.current_pos.next ## connect left  to right
            self.current_pos.next.prev = self.current_pos.prev ## connect right to left
            self.current_pos = self.current_pos.next
            self.size -= 1

    def get_value(self):
        """Returns the value of the item at the current position in the list (None if not item)"""
        if not self.current_pos:
            return None
        return self.current_pos.data

    def move_to_next(self):
        """Moves the current position one item closer to the tail/trailer.
        Do nothing if at end"""
        if self.current_pos != self.tail: # and self.current_pos is not None: # CHECK the if-statement
            self.current_pos = self.current_pos.next

    def move_to_prev(self):
        """Moves the current position one item closer to the head/header.
        Do nothing if at beginning"""
        if self.current_pos.prev != self.head:
            self.current_pos = self.current_pos.prev

    def move_to_pos(self, pos):
        """Moves the current position to item #position in the list.
        The first actual data item is #0"""
        # if (self.size != 0) and (0 <= pos < self.size):
        #     index = 0
        #     self.current_pos = self.head.next
        #     while index != pos: 
        #         self.current_pos = self.current_pos.next
        #         index += 1

        if pos < 0 or pos >= self.size:
            return
        self.current_pos = self.head.next
        for x in range(pos):
            self.move_to_next()

    def clear(self): # HELP
        """Clears all nodes from the list"""
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.current_pos = self.tail

    def get_first_node(self):
        """Returns the first Node (not the value) of the list """
        if self.size == 0:
            return None
        return self.head.next

    def get_last_node(self):
        """Returns the last Node (not the value) of the list"""
        if self.size == 0:
            return None
        return self.tail.prev


    def partition(self, low, high): #  JB CHECK -- base case
        """Loops from low to high and moves all nodes smaller than low so they are ahead (left side) of the low node"""
        if low == high or self.size == 0:
            return
        

        # pivot = low
        # low_data = low.data
        # while pivot != high.next:
        #     # check if "temp" is smaller than "low"
        #     if pivot.data < low_data:

        #         temp_data = pivot.data
        #         pivot.data = low_data
        #         pivot.prev.data = temp_data

        #     pivot = pivot.next
        # self.current_pos = low
        # return self.current_pos
    
        
        pivot = low
        while pivot != high.next:
            # check if "temp" is smaller than "low"
            if pivot.data < low.data:
                # put the temp node to in front of "low"
                self.current_pos = low
                self.insert(pivot.data)
                # severe the temp node from the original position
                self.current_pos = pivot
                self.remove()
            pivot = pivot.next
        self.current_pos = low
        return self.current_pos








    def sort(self): # TODO
        """Order the items in the list (ascending order)"""

        low = self.get_first_node()
        high = self.get_last_node()
            
        self.quick_sort(low, high)

    def quick_sort(self, low, high):
        
        # base case
        if (low and high) and (low != high) and (low != high.next):

            # inductive step
            pivot = self.partition(low, high)
            # recursivly sort left side of "low"
            self.quick_sort(low, pivot.prev)
            # recursively sort right side of "low"
            self.quick_sort(pivot.next, high)


    def __len__(self):
        """Returns the number of items in the list"""
        return self.size

    def __str__(self):
        """Returns string with all the items in the list with a single space between them"""
        ret_str = ""
        node = self.head.next
        while node != self.tail:
            ret_str += f"{node.data} "
            node = node.next
        return ret_str
    
    


if __name__ == "__main__":
    # create tests here if you want
    # dll = DLL()

    # empty sort
    # dll.sort()
    # assert str(dll) == ""
    # assert dll.head.next == dll.tail
    # assert dll.tail.prev == dll.head
    # assert dll.size == 0
    # assert dll.current_pos == dll.tail

    # dll.insert(1)
    # dll.insert(6)
    # dll.insert(4)
    # dll.insert(3)
    # dll.insert(5)

    # # noraml sort
    # dll.sort()
    # assert str(dll) == "1 3 4 5 6 "

    # # array with 1 node sort
    # dll = DLL()
    # dll.insert(1)
    # dll.sort()
    # assert str(dll) == "1 "
    pass