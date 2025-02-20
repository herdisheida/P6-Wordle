from DLL_base.dll import DLL


def test_init():
    dll = DLL()
    
    assert dll.head.next == dll.tail
    assert dll.tail.prev == dll.head

    assert dll.current_pos == dll.tail
    assert dll.current_pos.prev == dll.head
    assert dll.size == 0


def test_insert(dll):
    # TEST insert(value)
    dll.insert("A")
    assert str(dll) == "A "
    assert dll.current_pos.data == "A"
    assert dll.current_pos.next.data == dll.tail.data
    assert dll.head.next.data == "A"
    assert dll.tail.prev.data == "A"
    assert dll.size == 1
    assert len(dll) == 1

    dll.insert("B")
    assert str(dll) == "B A "
    assert dll.current_pos.data == "B"
    assert dll.current_pos.next.data == "A"
    assert dll.head.next.data == "B"
    assert dll.tail.prev.data == "A"
    assert dll.size == 2
    assert len(dll) == 2

    dll.insert("C")
    assert str(dll) == "C B A "
    assert dll.current_pos.data == "C"
    assert dll.current_pos.next.data == "B"
    assert dll.head.next.data =="C"
    assert dll.tail.prev.data == "A"
    assert dll.size == 3
    assert len(dll) == 3

def test_remove(dll):
    # testing remove()
    dll.remove()
    assert str(dll) == "B A "
    assert dll.current_pos.data == "B"
    assert dll.current_pos.next.data == "A"
    assert dll.head.next.data == "B"

    dll.remove()
    assert str(dll) == "A "
    assert dll.current_pos.data == "A"
    assert dll.current_pos.next.data == dll.tail.data
    assert dll.head.next.data == "A"

    dll.remove() # removing from 1 elem list
    assert str(dll) == ""
    assert dll.current_pos.data == dll.tail.data
    assert dll.current_pos.next == None
    assert dll.head.next.data == dll.tail.data

    dll.remove() # remove from empty array
    assert str(dll) == ""
    assert dll.current_pos.data == dll.tail.data
    assert dll.current_pos.next == None
    assert dll.head.next.data == dll.tail.data

def test_insert_and_remove():
    dll = DLL()
    
    # testing insert() and remove() together
    dll.insert("D")
    assert str(dll) == "D "
    dll.remove()
    assert str(dll) == ""
    assert dll.size == 0

    dll.insert("E")
    dll.insert("F")
    dll.insert("G")
    assert str(dll) == "G F E "
    dll.remove()
    assert str(dll) == "F E "
    dll.remove()
    assert str(dll) == "E "
    dll.remove()
    assert str(dll) == ""
    assert dll.size == 0

    # edge case: insert and remove right away multiple times
    dll.insert("H")
    assert str(dll) == "H "
    dll.remove()
    assert str(dll) == ""
    dll.insert("I")
    assert str(dll) == "I "
    dll.remove()
    assert str(dll) == ""
    dll.insert("J")
    assert str(dll) == "J "
    dll.remove()
    assert str(dll) == ""
    assert dll.size == 0

    # edge case: remove from empty list
    dll.remove()
    assert str(dll) == ""
    assert dll.size == 0

    # edge case: insert multiple and remove all
    dll.insert("K")
    dll.insert("L")
    dll.insert("M")
    dll.insert("N")
    assert str(dll) == "N M L K "
    dll.remove()
    dll.remove()
    dll.remove()
    dll.remove()
    assert str(dll) == ""
    assert dll.size == 0

def test_get_value():
    dll = DLL()
    value = dll.get_value()
    assert value == None
    
    dll.remove()
    value = dll.get_value()
    assert value == None

    dll.insert("A")
    value = dll.get_value()
    assert value == "A"

    dll.insert("B")
    value = dll.get_value()
    assert value == "B"

    dll.insert("C")
    value = dll.get_value()
    assert value == "C"

    dll.remove()
    value = dll.get_value()
    assert value == "B"

    dll.remove()
    value = dll.get_value()
    assert value == "A"

    dll.remove()
    value = dll.get_value()
    assert value == None

def test_move_to_next_and_move_to_prev():
    dll = DLL()

    # testing the empty list
    assert dll.current_pos == dll.tail
    dll.move_to_next()
    assert dll.current_pos == dll.tail
    dll.move_to_prev
    assert dll.current_pos == dll.tail


    assert dll.current_pos.data == None
    dll.insert("A")
    dll.insert("B")
    dll.insert("C")
    dll.insert("D")
    dll.insert("E")

    # MOVE NEXT
    assert dll.current_pos.data == "E"
    dll.move_to_next()
    assert dll.current_pos.data == "D"
    dll.move_to_next()
    assert dll.current_pos.data == "C"
    dll.move_to_next()
    assert dll.current_pos.data == "B"
    dll.move_to_next()
    assert dll.current_pos.data == "A"
    # checking the end
    dll.move_to_next()
    assert dll.current_pos == dll.tail # allow to go to the tail -- but not after that
    dll.move_to_next()
    assert dll.current_pos == dll.tail


    # MOVE PREV
    dll.move_to_prev()    
    assert dll.current_pos.data == "A"
    dll.move_to_prev()
    assert dll.current_pos.data == "B"
    dll.move_to_prev()
    assert dll.current_pos.data == "C"
    dll.move_to_prev()
    assert dll.current_pos.data == "D"
    dll.move_to_prev()
    assert dll.current_pos.data == "E"
    # checking the end
    dll.move_to_prev()
    assert dll.current_pos.data == "E"

def test_move_to_pos():
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

    assert str(dll) == "E D C B A "

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

    dll.move_to_pos(5) # able to move to tail
    assert dll.current_pos.data == None # keeps current post - does nothing

    # testing out of bounds
    dll.move_to_pos(10)
    assert dll.current_pos.data == None # keeps current post - does nothing

    dll.move_to_pos(-1)
    assert dll.current_pos.data == None # keeps current pos - does nothing

def test_get_first_node_and_get_last_node():
    dll = DLL()

    # testing the empty
    assert dll.get_first_node() == None
    assert dll.get_last_node() == None

    # testing with 1 elem in list
    dll.insert("A")
    assert dll.get_first_node().data == "A"
    assert dll.get_last_node().data == "A"

    # testing with >2 elem in list
    dll.insert("B")
    assert dll.get_first_node().data == "B"
    assert dll.get_last_node().data == "A"
    dll.insert("C")
    assert dll.get_first_node().data == "C"
    assert dll.get_last_node().data == "A"
    dll.insert("D")
    assert dll.get_first_node().data == "D"
    assert dll.get_last_node().data == "A"
    dll.insert("E")
    assert dll.get_first_node().data == "E"
    assert dll.get_last_node().data == "A"

    # testing after removing
    dll.remove()
    assert dll.get_first_node().data == "D"
    assert dll.get_last_node().data == "A"
    dll.remove()
    assert dll.get_first_node().data == "C"
    assert dll.get_last_node().data == "A"
    dll.remove()
    assert dll.get_first_node().data == "B"
    assert dll.get_last_node().data == "A"
    dll.remove()
    assert dll.get_first_node().data == "A"
    assert dll.get_last_node().data == "A"
    dll.remove()
    assert dll.get_first_node() == None # doesn't have any data in array
    assert dll.get_last_node() == None # doesn't have any data in array

def test_partition():
    dll = DLL()
    # testing NORMAL
    dll.insert(1)
    dll.insert(6)
    dll.insert(4)
    dll.insert(3)
    dll.insert(5)
    assert str(dll) == "5 3 4 6 1 "

    # the output order needs to be "3 4 1 5 6 "
    dll.partition(dll.get_first_node(), dll.get_last_node())
    

    # dæmið
    # "5 6 4 3 1"
    # "5 6 4 3 1"
    # "4 5 6 3 1"


    assert str(dll) == "3 4 1 5 6 "
    assert dll.head.next.data == 3
    assert dll.head.next.next.data == 4
    assert dll.get_first_node().data == 3
    assert dll.get_last_node().data == 6
    assert dll.tail.prev.data == 6
    assert dll.tail.prev.prev.data == 5

    # testing empty
    dll = DLL()
    dll.partition(dll.get_first_node(), dll.get_last_node())
    assert str(dll) == ""
    assert dll.head.next == dll.tail
    assert dll.get_first_node() == None
    assert dll.get_last_node() == None
    assert dll.tail.prev == dll.head

    # testing array with 1 node
    dll.insert(1)
    dll.partition(dll.get_first_node(), dll.get_last_node())
    assert str(dll) == "1 "
    assert dll.head.next.data == 1
    assert dll.get_first_node().data == 1
    assert dll.get_last_node().data == 1
    assert dll.head.next.next == dll.tail
    assert dll.tail.prev.prev == dll.head
    assert dll.current_pos.data == 1

    # testing array with 2 nodes::     3 -> 1 becomes 1 -> 3
    dll.insert(3)
    dll.partition(dll.get_first_node(), dll.get_last_node())
    assert str(dll) == "1 3 "
    assert dll.head.next.data == 1
    assert dll.head.next.next.data == 3
    assert dll.tail.prev.data == 3
    assert dll.tail.prev.prev.data == 1
    assert dll.get_first_node().data == 1
    assert dll.get_last_node().data == 3
    assert dll.head.next.next.next == dll.tail
    assert dll.tail.prev.prev.prev == dll.head
    # testing array with 2 nodes::     1 -> 3 becomes 1 -> 3
    dll = DLL()
    dll.insert(3)
    dll.insert(1)
    dll.partition(dll.get_first_node(), dll.get_last_node())
    assert str(dll) == "1 3 "
    assert dll.head.next.data == 1
    assert dll.head.next.next.data == 3
    assert dll.tail.prev.data == 3
    assert dll.tail.prev.prev.data == 1
    assert dll.get_first_node().data == 1
    assert dll.get_last_node().data == 3
    assert dll.head.next.next.next == dll.tail
    assert dll.tail.prev.prev.prev == dll.head
    # testing array with 2 nodes::     3 -> 3 becomes 3 -> 3
    dll = DLL()
    dll.insert(3)
    dll.insert(3)
    dll.partition(dll.get_first_node(), dll.get_last_node())
    assert str(dll) == "3 3 "
    assert dll.head.next.data == 3
    assert dll.head.next.next.data == 3
    assert dll.tail.prev.data == 3
    assert dll.tail.prev.prev.data == 3
    assert dll.get_first_node().data == 3
    assert dll.get_last_node().data == 3
    assert dll.head.next.next.next == dll.tail
    assert dll.tail.prev.prev.prev == dll.head


    # testing high and low where they're not the first and last nodes in the array
    dll = DLL()
    dll.insert(1)
    dll.insert(6)
    dll.insert(4)
    dll.insert(3)
    dll.insert(5)

    assert str(dll) == "5 3 4 6 1 "
    dll.partition(dll.get_first_node(), dll.get_last_node().prev.prev.prev)
    assert str(dll) == "3 5 4 6 1 "
    assert dll.current_pos.data == 5 # should be pointing towards the pivot (low)
    dll.partition(dll.get_first_node().next.next, dll.get_last_node())
    assert str(dll) == "3 5 1 4 6 "
    assert dll.current_pos.data == 4 # should be pointing towards the pivot (low)
    


def test_sort():
    dll = DLL()
    assert dll.head.next == dll.tail
    assert dll.tail.prev == dll.head
    assert dll.current_pos == dll.tail


    # empty sort
    dll.sort()
    assert str(dll) == ""
    assert dll.size == 0
    assert dll.head.next == dll.tail
    assert dll.tail.prev == dll.head
    assert dll.current_pos == dll.tail

    dll.insert(1)
    dll.insert(6)
    dll.insert(4)
    dll.insert(3)
    dll.insert(5)

    # noraml sort
    assert str(dll) == "5 3 4 6 1 "
    dll.sort()
    assert str(dll) == "1 3 4 5 6"


    # array with 1 node sort
    dll = DLL()
    dll.insert(1)
    dll.sort()
    assert str(dll) == "1 "
    assert dll.size == 1
    assert dll.head.next.data == 1
    assert dll.tail.prev.data == 1
    assert dll.current_pos.data == 1
    # empty after removing
    dll.remove()
    dll.sort()
    assert str(dll) == ""
    assert dll.size == 0
    assert dll.head.next == dll.tail
    assert dll.tail.prev == dll.head
    assert dll.current_pos == dll.tail

def test_current_node_rules():
    dll = DLL()
    assert dll.current_pos != dll.head  # current node should not be head
    assert dll.current_pos == dll.tail  # current node can be tail

    dll.insert("A")
    assert dll.current_pos != dll.head  # current node should not be head
    assert dll.current_pos != dll.tail  # current node should not be tail after insert

    dll.move_to_next()
    assert dll.current_pos == dll.tail  # current node can be tail
    dll.move_to_next()
    assert dll.current_pos == dll.tail  # current node can be tail

    dll.move_to_prev()
    assert dll.current_pos != dll.head  # current node should not be head
    assert dll.current_pos != dll.tail  # current node should not be tail after move_to_prev
    dll.move_to_prev()
    assert dll.current_pos != dll.head  # current node should not be head
    assert dll.current_pos != dll.tail  # current node should not be tail after move_to_prev

def test_all_together():
    dll = DLL()

    # Test initialization
    assert dll.head.next == dll.tail
    assert dll.tail.prev == dll.head
    assert dll.current_pos == dll.tail
    assert dll.size == 0

    # Test insertions
    dll.insert("A")
    assert str(dll) == "A "
    dll.insert("B")
    assert str(dll) == "B A "
    dll.insert("C")
    assert str(dll) == "C B A "
    assert dll.size == 3

    # Test removals
    dll.remove()
    assert str(dll) == "B A "
    dll.remove()
    assert str(dll) == "A "
    dll.remove()
    assert str(dll) == ""
    assert dll.size == 0

    # Test get_value
    dll.insert("A")
    assert dll.get_value() == "A"
    dll.insert("B")
    assert dll.get_value() == "B"
    dll.remove()
    assert dll.get_value() == "A"
    dll.remove()
    assert dll.get_value() == None

    # Test move_to_next and move_to_prev
    dll.insert("A")
    dll.insert("B")
    dll.insert("C")
    dll.move_to_next()
    assert dll.current_pos.data == "B"
    dll.move_to_next()
    assert dll.current_pos.data == "A"
    dll.move_to_next()
    assert dll.current_pos == dll.tail
    dll.move_to_prev()
    assert dll.current_pos.data == "A"
    dll.move_to_prev()
    assert dll.current_pos.data == "B"
    dll.move_to_prev()
    assert dll.current_pos.data == "C"
    dll.move_to_prev()
    assert dll.current_pos.data == "C"

    # Test move_to_pos
    dll.move_to_pos(0)
    assert dll.current_pos.data == "C"
    dll.move_to_pos(1)
    assert dll.current_pos.data == "B"
    dll.move_to_pos(2)
    assert dll.current_pos.data == "A"
    dll.move_to_pos(3)
    assert dll.current_pos == dll.tail

    # Test get_first_node and get_last_node
    assert dll.get_first_node().data == "C"
    assert dll.get_last_node().data == "A"
    dll.remove()
    assert dll.get_last_node().data == "B"
    dll.remove()
    assert dll.get_last_node().data == "C"
    dll.remove()
    assert dll.get_last_node() == None

    # Test partition
    dll.insert(1)
    dll.insert(6)
    dll.insert(4)
    dll.insert(3)
    dll.insert(5)
    dll.partition(dll.get_first_node(), dll.get_last_node())
    assert str(dll) == "3 4 1 5 6 "

    # Test sort
    dll.sort()
    assert str(dll) == "1 3 4 5 6 "

    # Test clear
    dll.clear()
    assert str(dll) == ""
    assert dll.size == 0

    # Test edge cases
    dll.insert("A")
    dll.insert("B")
    dll.insert("C")
    dll.move_to_pos(10)
    assert dll.current_pos.data == "C"
    dll.move_to_pos(-1)
    assert dll.current_pos.data == "C"
    dll.remove()
    dll.remove()
    dll.remove()
    dll.remove()
    assert str(dll) == ""
    assert dll.size == 0

if __name__ == "__main__":
    dll = DLL()

    test_init()

    test_insert(dll)
    test_remove(dll)
    test_insert_and_remove()

    test_get_value()
    
    test_move_to_next_and_move_to_prev()
    test_move_to_pos()

    test_get_first_node_and_get_last_node()

    test_partition()
    test_sort()

    # test_all_together()

    print("All tests passed")