class ItemExistsException(Exception):
    pass
class NotFoundException(Exception):
    pass


class BST_Node():
    def __init__(self, key=None, data=None, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BSTMap():
    def __init__(self):
        self.root = BST_Node()


    def _insert_recur(self, node, key, data):
        if key == node.key:
            raise ItemExistsException()
        
        if key < node.key:
            if node.left == None:
                node.left = BST_Node(key, data)
            else:
                self._insert_recur(node.left, key, data)
        elif key > node.key:
            if node.right == None:
                node.right = BST_Node(key, data)
            else:
                self._insert_recur(node.right, key, data)

    def insert(self, key, data):
        """ Adds this value pair to the collection """
        if self.root.key == None:
            self.root = BST_Node(key, data)
        else:
            self._insert_recur(self.root, key, data)

    def update(self, key, data):
        """ Sets the data value of the value pair with equal key to data """
        data 
        # then change --- node.data = data

    def _find_recur(self, node, key):
        if node.key == key:
            return node.data
        
        if key < node.key:
            if node.left:
                return self._find_recur(node.left, key)
        elif key > node.key:
            if node.right:
                return self._find_recur(node.right, key)
        
    def find(self, key):
        """ Returns the data value of the value pair with equal key """
        if self.root.data == None:
            raise NotFoundException()
        
        data = self._find_recur(self.root, key)
        if not data:
            raise NotFoundException()
        return data
    

    def contains(self, key):
        """ Returns True if equal key is found in the collection, otherwise False """
        pass

    def remove(self, key):
        """ Removes the value pair with equal key from the collection """
        pass

    def __setitem__(self, key, data):
        """ Adds this value pair to the collection """
        pass

    def __getitem__(self, key):
        """ Returns the data value of the value pair with equal key """
        # TA -- er þetta bara nákvæmlega það sama og find -- nema bara með bandstriks dæminu
        return self.find(key)

    def __len__(self):
        """ Returns the number of items in the entire data structure """
        pass

    def __str__(self):
        """ Returns a string with the items ordered by key and separated by a single space """
        return self._inorder_recur(self.root) if self.root.data else ""

    def _inorder_recur(self, node, ret=""):
        if node:
            ret = self._inorder_recur(node.left, ret)
            ret += f"{{{node.key}:{node.data}}} "
            ret = self._inorder_recur(node.right, ret)
        return ret
    


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
        print("Should be a NotFoundException()")
    # __getitem__
    try:
        bst[20]
    except NotFoundException:
        pass
    else:
        print("should be NotFoundException()")



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
        print("should be ItemExistsException()")
    try:
        bst.insert(18, "átjánmjátján")
    except ItemExistsException:
        pass
    else:
        print("should be ItemExistsException()")

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
        print("should be NotFoundException()")


    # UPDATE test
    bst.update(10, "tinnibinni")
    assert str(bst) == "{3:three} {5:five} {7:seven} {10:tinnibinni} {12:twelve} {15:fifteen} {18:eighteen} "
    bst.update(10, "tinni")
    assert str(bst) == "{3:three} {5:five} {7:seven} {10:tinni} {12:twelve} {15:fifteen} {18:eighteen} "
    bst.update(3, "þristur")
    assert str(bst) == "{3:þristur} {5:five} {7:seven} {10:tinni} {12:twelve} {15:fifteen} {18:eighteen} "
    bst.update(18, "HO")
    assert str(bst) == "{3:þristur} {5:five} {7:seven} {10:tinni} {12:twelve} {15:fifteen} {18:HO} "


    
    # # ...additional test cases if needed...
    pass
