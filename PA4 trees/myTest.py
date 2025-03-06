from BST import BSTMap, ItemExistsException, NotFoundException


def myTest():
    bst = BSTMap()

    # EMPTY tree test
    assert str(bst) == ""
    # assert bst.root.key == None
    assert bst.size == 0
    assert len(bst) == 0


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

    # remove empty
    try:
        bst.remove(10)
    except NotFoundException:
        pass
    else:
        print("remove empty tree : Should be a NotFoundException()")


    # INSERT test
    bst.insert(10, "ten")
    assert bst.root.key == 10
    assert bst.root.data == "ten"
    assert len(bst) == 1
    bst.insert(5, "five")
    assert bst.root.key == 10
    assert bst.root.left.key == 5
    assert len(bst) == 2
    bst.insert(15, "fifteen")
    assert bst.root.right.key == 15
    assert len(bst) == 3
    bst.insert(3, "three")
    assert bst.root.left.left.key == 3
    assert len(bst) == 4
    bst.insert(7, "seven")
    assert bst.root.left.right.key == 7
    assert len(bst) == 5
    bst.insert(12, "twelve")
    assert bst.root.right.left.key == 12
    assert len(bst) == 6
    bst.insert(18, "eighteen")
    assert bst.root.right.right.key == 18
    assert str(bst) == "output: {3:three} {5:five} {7:seven} {10:ten} {12:twelve} {15:fifteen} {18:eighteen}"
    assert len(bst) == 7

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
    assert len(bst) == 7

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
    assert len(bst) == 7
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
    assert bst.contains(50) == False


    # UPDATE test
    bst.update(10, "tinnibinni")
    assert str(bst) == "output: {3:three} {5:five} {7:seven} {10:tinnibinni} {12:twelve} {15:fifteen} {18:eighteen}"
    bst.update(10, "tinni")
    assert str(bst) == "output: {3:three} {5:five} {7:seven} {10:tinni} {12:twelve} {15:fifteen} {18:eighteen}"
    bst.update(3, "þristur")
    assert str(bst) == "output: {3:þristur} {5:five} {7:seven} {10:tinni} {12:twelve} {15:fifteen} {18:eighteen}"
    bst.update(18, "HO")
    assert str(bst) == "output: {3:þristur} {5:five} {7:seven} {10:tinni} {12:twelve} {15:fifteen} {18:HO}"

    # __setitem__ test
        # Changing data from existing key
    bst.__setitem__(10, "Mima")
    assert bst.find(10) == "Mima"
    assert bst[10] == "Mima"
    bst[10] = "JB"
    assert bst.find(10) == "JB"
    assert bst[10] == "JB"
    assert len(bst) == 7
        # Making new key with corresponding data
    bst[100] = "OH HE MASSIVE"
    assert bst.find(100) == "OH HE MASSIVE"
    assert bst[100] == "OH HE MASSIVE"
    assert len(bst) == 8
    bst[200] = "OH EVEN BIGGEr"
    assert bst.find(200) == "OH EVEN BIGGEr"
    assert bst[200] == "OH EVEN BIGGEr"
    assert len(bst) == 9


    # REMOVE test
    assert str(bst) == "output: {3:þristur} {5:five} {7:seven} {10:JB} {12:twelve} {15:fifteen} {18:HO} {100:OH HE MASSIVE} {200:OH EVEN BIGGEr}"


    # remove with 1 child
    bst.remove(100) # remove a node with no children
    assert len(bst) == 8
    assert str(bst) == "output: {3:þristur} {5:five} {7:seven} {10:JB} {12:twelve} {15:fifteen} {18:HO} {200:OH EVEN BIGGEr}"
  

    bst.remove(3) # remove a node with no children
    assert len(bst) == 7
    assert str(bst) == "output: {5:five} {7:seven} {10:JB} {12:twelve} {15:fifteen} {18:HO} {200:OH EVEN BIGGEr}"

    # find node that doesn't exsist
    try:
        bst.find(3)
    except NotFoundException:
        pass
    else:
        print("remove(3) [what we just removed] : should be a NotFoundException()")

    # remove node that doesn't exist
    try:
        bst.remove(3)
    except NotFoundException:
        assert len(bst) == 7, "size shouldn't change"
        pass
    else:
        print("remove(3) AGAIN [should not be in the tree] : should be a NotFoundException()")

    # find a key that doesn't exist
    try:
        bst.find(-10)
    except NotFoundException:
        pass
    else:
        print("remove(-10) non-existent key : should be a NotFoundException()")


    # remove root node
    bst.remove(10)
    assert len(bst) == 6
    assert str(bst) == "output: {5:five} {7:seven} {12:twelve} {15:fifteen} {18:HO} {200:OH EVEN BIGGEr}"



    print("ALL MyTest passed")

def COTest():
    bst = BSTMap()

    # Test inserting duplicate keys
    bst.insert(1, "one")
    try:
        bst.insert(1, "one_duplicate")
    except ItemExistsException:
        pass
    else:
        print("insert : should be ItemExistsException()")

    # Test updating non-existent key
    try:
        bst.update(2, "two")
    except NotFoundException:
        pass
    else:
        print("update : should be NotFoundException()")

    # Test removing non-existent key
    try:
        bst.remove(2)
    except NotFoundException:
        pass
    else:
        print("remove : should be NotFoundException()")

    # Test finding non-existent key
    try:
        bst.find(2)
    except NotFoundException:
        pass
    else:
        print("find : should be NotFoundException()")

    # Test __getitem__ for non-existent key
    try:
        bst[2]
    except NotFoundException:
        pass
    else:
        print("__getitem__ : should be NotFoundException()")

    # Test __setitem__ for updating existing key
    bst[1] = "one_updated"
    assert bst.find(1) == "one_updated"

    # Test __setitem__ for inserting new key
    bst[2] = "two"
    assert bst.find(2) == "two"

    # Test contains for existing and non-existing keys
    assert bst.contains(1) == True
    assert bst.contains(2) == True
    assert bst.contains(3) == False

    # Test removing root node
    bst.remove(1)
    assert bst.contains(1) == False

    # Test removing node with one child
    bst.insert(3, "three")
    bst.insert(4, "four")
    bst.remove(3)
    assert bst.contains(3) == False
    assert bst.contains(4) == True

    # Test removing node with two children
    bst.insert(5, "five")
    bst.insert(6, "six")
    bst.insert(7, "seven")
    bst.remove(5)
    assert bst.contains(5) == False
    assert bst.contains(6) == True
    assert bst.contains(7) == True

    print("ALL COTest passed")
    

if __name__ == "__main__":
    myTest()
    COTest()
