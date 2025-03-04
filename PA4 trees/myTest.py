from BST import BSTMap, ItemExistsException, NotFoundException


if __name__ == "__main__":
    bst = BSTMap()

    # EMPTY tree test
    assert str(bst) == ""
    assert bst.root.key == None

    # find()
    try:
        bst.find(10) == "á ekki að finna"
    except NotFoundException:
        pass
    else:
        print("find : Should be a NotFoundException()")

    # contains
    bst.contains(10) == False

    # __getitem__
    try:
        bst[20]
    except NotFoundException:
        pass
    else:
        print("__getitem__ : should be NotFoundException()")



    # INSERT test
    bst.insert(10, "ten")
    assert bst.root.key == 10
    assert bst.root.data == "ten"
    bst.insert(5, "five")
    assert bst.root.key == 10
    assert bst.root.left.key == 5
    bst.insert(15, "fifteen")
    assert bst.root.right.key == 15
    bst.insert(3, "three")
    assert bst.root.left.left.key == 3
    bst.insert(7, "seven")
    assert bst.root.left.right.key == 7
    bst.insert(12, "twelve")
    assert bst.root.right.left.key == 12
    bst.insert(18, "eighteen")
    assert bst.root.right.right.key == 18
    assert str(bst) == "{3:three} {5:five} {7:seven} {10:ten} {12:twelve} {15:fifteen} {18:eighteen} "
    
    # INSERT ItemExistsException()
    try:
        bst.insert(10, "tíamía")
    except ItemExistsException:
        pass
    else:
        print("insert : should be ItemExistsException()")
    try:
        bst.insert(18, "átjánmjátján")
    except ItemExistsException:
        pass
    else:
        print("insert : should be ItemExistsException()")

    # FIND test
    assert bst.find(10) == "ten"
    assert bst.find(5) == "five"
    assert bst.find(15) == "fifteen"
    assert bst.find(3) == "three"
    assert bst.find(7) == "seven"
    assert bst.find(12) == "twelve"
    assert bst.find(18) == "eighteen"

    # FIND NotFoundException()
    try:
        bst.find(20)
    except NotFoundException:
        pass
    else:
        print("should be NotFoundException()")


    # __getitem__ test
    assert bst[10] == "ten"
    assert bst[5] == "five"
    assert bst[15] == "fifteen"
    assert bst[3] == "three"
    assert bst[7] == "seven"
    assert bst[12] == "twelve"
    assert bst[18] == "eighteen"
    # something not in the tree
    try:
        bst[20]
    except NotFoundException:
        pass
    else:
        print("__getitem__ : Should be NotFoundException()")


    # contains
    assert bst.contains(10) == True
    assert bst.contains(5) == True
    assert bst.contains(15) == True
    assert bst.contains(3) == True
    assert bst.contains(7) == True
    assert bst.contains(12) == True
    assert bst.contains(18) == True
    # does not contains
    assert bst.contains(0) == False




    # UPDATE test
    # bst.update(10, "tinnibinni")
    # assert str(bst) == "{3:three} {5:five} {7:seven} {10:tinnibinni} {12:twelve} {15:fifteen} {18:eighteen} "
    # bst.update(10, "tinni")
    # assert str(bst) == "{3:three} {5:five} {7:seven} {10:tinni} {12:twelve} {15:fifteen} {18:eighteen} "
    # bst.update(3, "þristur")
    # assert str(bst) == "{3:þristur} {5:five} {7:seven} {10:tinni} {12:twelve} {15:fifteen} {18:eighteen} "
    # bst.update(18, "HO")
    # assert str(bst) == "{3:þristur} {5:five} {7:seven} {10:tinni} {12:twelve} {15:fifteen} {18:HO} "


    
    # # ...additional test cases if needed...
    pass
