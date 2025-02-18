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
        if self.size == 0:
            self.head.next = node
            self.tail.prev = node
        else:
            self.current_pos.prev.next = node # connect left to newNode (left->new)
            self.current_pos.prev = node # connect right to newNode (new<-right)
        self.current_pos = node
        self.size += 1

        
    def remove(self):
        """Removes the node at the current position if there is one (otherwise does nothing)"""
        if self.size == 0:
            return
        self.current_pos.prev.next = self.current_pos.next ## connect left to right
        self.current_pos.next.prev = self.current_pos.prev ## connect right to left
        self.current_pos = self.current_pos.next
        self.size -= 1

    def get_value(self):
        """Returns the value of the item at the current position in the list (None if not item)"""
        if self.size == 0:
            return None
        return self.current_pos.data

    def move_to_next(self):
        """Moves the current position one item closer to the tail/trailer.
        Do nothing if at end"""
        if self.current_pos.next == self.tail or self.size == 0:
            return
        self.current_pos = self.current_pos.next

    def move_to_prev(self):
        """Moves the current position one item closer to the head/header.
        Do nothing if at beginning"""
        if self.current_pos.prev != self.head:
            self.current_pos = self.current_pos.prev

    def move_to_pos(self, pos):
        """Moves the current position to item #position in the list.
        The first actual data item is #0"""
        if self.size != 0 and (0 <= pos < self.size):
            index = 0
            self.current_pos = self.head.next
            while index != pos: 
                self.current_pos = self.current_pos.next
                index += 1
        
    def clear(self):
        """Clears all nodes from the list"""
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.current_pos = self.tail # CHECK
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
        ret_str = ""
        node = self.head.next
        while node != self.tail:
            ret_str += f"{node.data} "
            node = node.next
        return ret_str
    
    


if __name__ == "__main__":
    # create tests here if you want

    dll = DLL()

    # testing empty
    dll.move_to_pos(-1)
    assert dll.current_pos == dll.tail
    dll.move_to_pos(0)
    assert dll.current_pos == dll.tail
    dll.move_to_pos(1)
    assert dll.current_pos == dll.tail


    dll.insert("A")
    dll.insert("B")
    dll.insert("C")
    dll.insert("D")
    dll.insert("E")


    dll.move_to_pos(-1)
    assert dll.current_pos.data == "E" # keeps current pos - does nothing
    dll.move_to_pos(0)
    assert dll.current_pos.data == "E"
    dll.move_to_pos(1)
    assert dll.current_pos.data == "D"
    dll.move_to_pos(2)
    assert dll.current_pos.data == "C"
    dll.move_to_pos(3)
    assert dll.current_pos.data == "B"
    dll.move_to_pos(4)
    assert dll.current_pos.data == "A"

    # testing out of bounds
    dll.move_to_pos(5)
    assert dll.current_pos.data == "A" # keeps current post - does nothing


    # testing get_value()
