from pa2_base.QueueStackBase.my_linked_list import LinkedList



def pushBack_then_pushFront(ll):
    """ TESTING push_back() on an empty list,
    and then push_front() into a non-empty list"""

    # PUSH BACK TEST
    ll.push_back(1)
    assert ll.head.data == 1 # HEAD
    assert ll.tail.data == 1 # TAIL
    assert ll.head.next == None # AFTER HEAD
    assert ll.get_size() == 1 # SIZE func
    assert str(ll) == "1 " # CHECK WHOLE LIST
    ll.push_back(2)
    assert ll.head.data == 1 # HEAD
    assert ll.tail.data == 2 # TAIL
    assert ll.head.next.data == 2 # AFTER HEAD
    assert ll.get_size() == 2 # SIZE func
    assert str(ll) == "1 2 " # CHECK WHOLE LIST
    ll.push_back(3)
    assert ll.head.data == 1 # HEAD
    assert ll.tail.data == 3 # TAIL
    assert ll.head.next.data == 2 # AFTER HEAD
    assert ll.get_size() == 3 # SIZE func
    assert str(ll) == "1 2 3 " # CHECK WHOLE LIST
    ll.push_back(4)
    assert ll.head.data == 1 # HEAD
    assert ll.tail.data == 4 # TAIL
    assert ll.head.next.data == 2 # AFTER HEAD
    assert ll.head.next.next.data == 3 # AFTER AFTER HEAD
    assert ll.head.next.next.next.data == 4 # AFTER AFTER AFTER HEAD
    assert ll.head.next.next.next.next == None # AFTER AFTER AFTER AFTER HEAD = AFTER TAIL
    assert ll.get_size() == 4 # SIZE func
    assert str(ll) == "1 2 3 4 " # CHECK WHOLE LIST


    # PUSH FRONT TEST
    ll.push_front(5)
    assert ll.head.data == 5 # HEAD
    assert ll.tail.data == 4 # TAIL
    assert ll.head.next.data == 1 # AFTER HEAD
    assert ll.get_size() == 5 # SIZE func
    assert str(ll) == "5 1 2 3 4 " # CHECK WHOLE LIST
    ll.push_front(6)
    assert ll.head.data == 6 # HEAD
    assert ll.tail.data == 4 # TAIL
    assert ll.head.next.data == 5 # AFTER HEAD
    assert ll.get_size() == 6 # SIZE func
    assert str(ll) == "6 5 1 2 3 4 " # CHECK WHOLE LIST
    ll.push_front(7)
    assert ll.head.data == 7 # HEAD
    assert ll.tail.data == 4 # TAIL
    assert ll.head.next.data == 6 # AFTER HEAD
    assert ll.get_size() == 7 # SIZE func
    assert str(ll) == "7 6 5 1 2 3 4 " # CHECK WHOLE LIST
    ll.push_front(8)
    assert ll.head.data == 8 # HEAD
    assert ll.tail.data == 4 # TAIL
    assert ll.head.next.data == 7 # AFTER HEAD
    assert ll.get_size() == 8 # SIZE func
    assert str(ll) == "8 7 6 5 1 2 3 4 " # CHECK WHOLE LIST

def pushFront_then_pushBack(ll):
    """ TESTING push_front() on an empty list,
    and then push_back() into a non-empty list"""

    # PUSH FRONT TEST
    ll.push_front(1)
    assert ll.head.data == 1 # HEAD
    assert ll.tail.data == 1 # TAIL
    assert ll.head.next == None # AFTER HEAD
    assert ll.get_size() == 1 # SIZE func
    assert str(ll) == "1 " # CHECK WHOLE LIST'
    ll.push_front(2)
    assert ll.head.data == 2 # HEAD
    assert ll.tail.data == 1 # TAIL
    assert ll.head.next.data == 1 # AFTER HEAD
    assert ll.get_size() == 2 # SIZE func
    assert str(ll) == "2 1 " # CHECK WHOLE LIST'
    ll.push_front(3)
    assert ll.head.data == 3 # HEAD
    assert ll.tail.data == 1 # TAIL
    assert ll.head.next.data == 2 # AFTER HEAD
    assert ll.get_size() == 3 # SIZE func
    assert str(ll) == "3 2 1 " # CHECK WHOLE LIST'

    # PUSH BACK TEST
    ll.push_back(4)
    assert ll.head.data == 3 # HEAD
    assert ll.tail.data == 4 # TAIL
    assert ll.head.next.data == 2 # AFTER HEAD
    assert ll.get_size() == 4 # SIZE func
    assert str(ll) == "3 2 1 4 " # CHECK WHOLE LIST'
    ll.push_back(5)
    assert ll.head.data == 3 # HEAD
    assert ll.tail.data == 5 # TAIL
    assert ll.head.next.data == 2 # AFTER HEAD
    assert ll.get_size() == 5 # SIZE func
    assert str(ll) == "3 2 1 4 5 " # CHECK WHOLE LIST'
    ll.push_back(6)
    assert ll.head.data == 3 # HEAD
    assert ll.tail.data == 6 # TAIL
    assert ll.head.next.data == 2 # AFTER HEAD
    assert ll.get_size() == 6 # SIZE func
    assert str(ll) == "3 2 1 4 5 6 " # CHECK WHOLE LIST'

def pop_emptyList(ll):
    """ TESTING pop_front() and pop_back()
    on an empty list"""
    data = ll.pop_front()
    assert data == None
    assert str(ll) == ""
    data = ll.pop_back()
    assert data == None
    assert str(ll) == ""

def pop_list_with_oneElement(ll):
    """ TESTING pop_front() and pop_back()
    with only one element in the list"""

    # ADD 1 element - to begin the test
    ll.push_front(1)
    # POP FRONT TEST
    data = ll.pop_front()
    assert data == 1
    assert ll.head == None
    assert ll.tail == None
    assert ll.size == 0
    assert str(ll) == ""

    # ADD 1 element - to begin the test
    ll.push_front(1)
    data = ll.pop_back()
    assert data == 1
    # POP BACK TEST
    assert ll.head == None
    assert ll.tail == None
    assert ll.size == 0
    assert str(ll) == ""

def pop_nonEmptyList(ll):
    """ TESTING pop_front() and pop_back()
    on a non-empty list"""

    # POP FRONT TEST
    data = ll.pop_front()
    assert data == 3
    assert str(ll) == "2 1 4 5 6 "
    assert ll.head.data == 2
    assert ll.head.next.data == 1
    assert ll.tail.data == 6
    data = ll.pop_front()
    assert data == 2
    assert str(ll) == "1 4 5 6 "
    assert ll.head.data == 1
    assert ll.head.next.data == 4
    assert ll.tail.data == 6

    # POP BACK TEST
    data = ll.pop_back()
    assert data == 6
    assert str(ll) == "1 4 5 "
    assert ll.head.data == 1
    assert ll.head.next.data == 4
    assert ll.tail.data == 5
    data = ll.pop_back()
    assert data == 5
    assert str(ll) == "1 4 "
    assert ll.head.data == 1
    assert ll.head.next.data == 4
    assert ll.tail.data == 4


def test_LinkedList_Class():
    """ TESTING LinkedList as a whole:

    -- popping empty
     pop_front()
     pop_back()

    -- push_back right after push_front
     push_front()
     push_back()
     push_front()
     push_back()
    
    -- push_front right after push_back
     push_back()
     push_front()
     push_back()
     push_front()

    -- pop right after pushing
     push_back()
     pop_back()
     push_front()
     pop_front()

     push_back()
     pop_front()
     push_front()
     pop_back()
     """
    test = LinkedList()
    assert str(test) == ""

    # -- popping empty
    data = test.pop_front()
    assert data == None
    assert str(test) == ""
    data = test.pop_back()
    assert data == None
    assert str(test) == ""


    # -- push_back right after push_front
    test.push_front("A")
    assert str(test) == "A "
    assert test.head.data == "A"
    assert test.tail.data == "A"
    test.push_back("B")
    assert str(test) == "A B "
    assert test.head.data == "A"
    assert test.head.next.data == "B"
    assert test.tail.data == "B"
    assert test.tail.next == None
    test.push_front("C")
    assert str(test) == "C A B "
    assert test.head.data == "C"
    assert test.head.next.data == "A"
    assert test.tail.data == "B"
    assert test.tail.next == None
    test.push_back("D")
    assert str(test) == "C A B D "
    assert test.head.data == "C"
    assert test.head.next.data == "A"
    assert test.tail.data == "D"
    assert test.tail.next == None


    test = LinkedList() # RESET TO begin empty
    assert str(test) == ""
    # -- push_front right after push_back
    test.push_back("A")
    assert str(test) == "A "
    assert test.head.data == "A"
    assert test.tail.data == "A"
    test.push_front("B")
    assert str(test) == "B A "
    assert test.head.data == "B"
    assert test.head.next.data == "A"
    assert test.tail.data == "A"
    assert test.tail.next == None
    test.push_back("C")
    assert str(test) == "B A C "
    assert test.head.data == "B"
    assert test.head.next.data == "A"
    assert test.tail.data == "C"
    assert test.tail.next == None
    test.push_front("D")
    assert str(test) == "D B A C "
    assert test.head.data == "D"
    assert test.head.next.data == "B"
    assert test.tail.data == "C"
    assert test.tail.next == None


    test = LinkedList() # RESET TO begin empty
    assert str(test) == ""
    # -- pop_back right after push_back
    test.push_back(1)
    assert str(test) == "1 "
    assert test.head.data == 1
    assert test.tail.data == 1
    assert test.head.next == None
    data = test.pop_back()
    assert str(test) == ""
    assert test.head == None
    assert test.tail == None
    test.push_front(2)
    assert str(test) == "2 "
    assert test.head.data == 2
    assert test.tail.data == 2
    assert test.head.next == None
    data = test.pop_front()
    assert str(test) == ""
    assert test.head == None
    assert test.tail == None

    # -- pop_front right after push_front
    test.push_back(1)
    assert str(test) == "1 "
    assert test.head.data == 1
    assert test.tail.data == 1
    assert test.head.next == None
    data = test.pop_front()
    assert str(test) == ""
    assert test.head == None
    assert test.tail == None
    test.push_front(2)
    assert str(test) == "2 "
    assert test.head.data == 2
    assert test.tail.data == 2
    assert test.head.next == None
    data = test.pop_back()
    assert str(test) == ""
    assert test.head == None
    assert test.tail == None


    # -- pop_back() with 2 nodes
    test.push_front(1) # initalize the 2 nodes
    test.push_back(2) # initalize the 2 nodes
    assert str(test) == "1 2 "
    assert test.head.data == 1
    assert test.head.next == test.tail
    assert test.tail.data == 2
        # begin popping_back
    data = test.pop_back()
    assert str(test) == "1 "
    assert data == 2
    assert test.head.data == 1
    assert test.tail.data == 1
    assert test.head.next == None
    assert test.tail.next == None

def final_testing():
    """ Comprehensive testing of LinkedList operations, including edge cases. """
    ll = LinkedList()

    # Test on empty list
    assert ll.pop_front() == None
    assert ll.pop_back() == None
    assert ll.get_size() == 0
    assert str(ll) == ""

    # Test push_back on empty list
    ll.push_back(1)
    assert ll.head.data == 1
    assert ll.tail.data == 1
    assert ll.get_size() == 1
    assert str(ll) == "1 "

    # Test push_front on non-empty list
    ll.push_front(0)
    assert ll.head.data == 0
    assert ll.tail.data == 1
    assert ll.get_size() == 2
    assert str(ll) == "0 1 "

    # Test pop_front on non-empty list
    assert ll.pop_front() == 0
    assert ll.head.data == 1
    assert ll.tail.data == 1
    assert ll.get_size() == 1
    assert str(ll) == "1 "

    # Test pop_back on non-empty list
    assert ll.pop_back() == 1
    assert ll.head == None
    assert ll.tail == None
    assert ll.get_size() == 0
    assert str(ll) == ""

    # Test push_back and push_front alternately
    ll.push_back(1)
    ll.push_front(0)
    ll.push_back(2)
    ll.push_front(-1)
    assert str(ll) == "-1 0 1 2 "
    assert ll.get_size() == 4

    # Test pop_front and pop_back alternately
    assert ll.pop_front() == -1
    assert ll.pop_back() == 2
    assert str(ll) == "0 1 "
    assert ll.get_size() == 2

    # Test edge case with multiple elements
    ll.push_back(2)
    ll.push_back(3)
    ll.push_back(4)
    assert str(ll) == "0 1 2 3 4 "
    assert ll.get_size() == 5

    # Pop all elements to test stability
    assert ll.pop_front() == 0
    assert ll.pop_front() == 1
    assert ll.pop_front() == 2
    assert ll.pop_front() == 3
    assert ll.pop_front() == 4
    assert ll.pop_front() == None
    assert ll.pop_back() == None
    assert str(ll) == ""
    assert ll.get_size() == 0

    print("All final tests passed")

if __name__ == "__main__":
    ll = LinkedList()
    ll2 = LinkedList()

    pop_emptyList(ll)
    pop_list_with_oneElement(ll)
    pushBack_then_pushFront(ll2) # push_back on an emptyList
    pushFront_then_pushBack(ll) # push_front on an emptyList
    pop_nonEmptyList(ll) # only works with

    test_LinkedList_Class() # WHOLE SHIT TOGETHER
    final_testing()
    print("All tests passed")
