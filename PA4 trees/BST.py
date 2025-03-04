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
        if key < node.key:
            if node.left == None:
                node.left = BST_Node(key, data)
            else:
                self._insert_recur(node.left, key, data)
        else:
            if node.right == None:
                node.right = BST_Node(key, data)
            else:
                self._insert_recur(node.right, key, data)


        return # don't insert if the data already exists 

    def insert(self, key, data):
        """ Adds this value pair to the collection """
        if self.root.key == None:
            self.root = BST_Node(key, data)
        else:
            self._insert_recur(self.root, key, data)

    def update(self, key, data):
        """ Sets the data value of the value pair with equal key to data """
        pass

    def find(self, key):
        """ Returns the data value of the value pair with equal key """
        pass

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
        pass

    def __len__(self):
        """ Returns the number of items in the entire data structure """
        pass

    def __str__(self):
        """ Returns a string with the items ordered by key and separated by a single space """
        return self._inorder_recur(self.root)

    def _inorder_recur(self, node, ret=""):
        if node:
            ret = self._inorder_recur(node.left, ret)
            ret += str(node.data) + " "
            ret = self._inorder_recur(node.right, ret)
        return ret

if __name__ == "__main__":
    bst = BSTMap()
    bst.insert(10, "ten")
    bst.insert(5, "five")
    bst.insert(15, "fifteen")
    bst.insert(3, "three")
    bst.insert(7, "seven")
    bst.insert(12, "twelve")
    bst.insert(18, "eighteen")

    print(bst)  # Expected output: "three five seven ten twelve fifteen eighteen"
    
    # # ...additional test cases if needed...
    pass
