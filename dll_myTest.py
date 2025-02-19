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
    assert dll.current_pos.data == "A"

    # MOVE RIGHT
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
    dll.move_to_pos(-1)
    assert dll.current_pos.data == "A" # keeps current pos - does nothing

def test_get_first_node_and_get_last_node():
    dll = DLL()

    # testing the empty
    node = dll.get_first_node()
    assert node == None
    node = dll.get_last_node()
    assert node == None

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

    print("All tests passed")