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
        if self.current_pos != self.tail:
            self.current_pos = self.current_pos.next

    def move_to_prev(self):
        """Moves the current position one item closer to the head/header.
        Do nothing if at beginning"""
        if self.current_pos.prev != self.head:
            self.current_pos = self.current_pos.prev

    def move_to_pos(self, pos):
        """Moves the current position to item #position in the list.
        The first node with data is at position #0"""
        if pos < 0 or pos > self.size:
            return
        self.current_pos = self.head.next
        for x in range(pos):
            self.current_pos = self.current_pos.next

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


    def partition(self, low, high):
        """Loops from low to high and moves all nodes smaller than low so they are ahead (left side) of the low node"""
        if self.size == 0: # empty array
            return
        if low == high: # 1 node in array
            self.current_pos = low
            return

        pivot = low
        temp = pivot.next
        
        while temp != high.next:
            # check if "temp" is smaller than "pivot"
            if temp.data < pivot.data:
                # move the temp node in front of pivot
                self.current_pos = pivot
                self.insert(temp.data)
                # severe the temp node from the original position
                self.current_pos = temp
                self.remove()
            temp = temp.next
        self.current_pos = pivot


    def sort(self):
        """Order the items in the list (ascending order)"""

        low = self.get_first_node()
        high = self.get_last_node()
            
        self.quick_sort(low, high)
        self.current_pos = self.head.next

    def quick_sort(self, low, high):
        
        # base case
        # if not low or not high or low == high or low.prev == high:
        #     return

        if low and high and low != high and low != high.next:
            # inductive step
            self.partition(low, high)
            # recursivly sort left side of "pivot"
            self.quick_sort(low, self.current_pos.prev)
            # recursively sort right side of "pivot"
            self.quick_sort(self.current_pos.next, high)


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
    pass
