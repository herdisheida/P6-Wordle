from pa2_base.QueueStackBase.my_linked_list import LinkedList



def push_back_then_front(ll):
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


def push_front_then_back(ll):
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



if __name__ == "__main__":
    ll = LinkedList()

    # push_back_then_front(ll)
    push_front_then_back(ll)

    print(ll)

