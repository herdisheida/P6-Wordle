from DLL_base.dll import DLL

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



if __name__ == "__main__":
    test_insert_and_remove()