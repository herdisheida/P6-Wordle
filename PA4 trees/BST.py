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
        self.size = 0 # TA má initalize size ?
        

    def _insert_recur(self, node, key, data):
        if key == node.key:
            raise ItemExistsException()
        
        if key < node.key:
            if node.left == None:
                node.left = BST_Node(key, data)
                self.size += 1
            else:
                self._insert_recur(node.left, key, data)
        elif key > node.key:
            if node.right == None:
                node.right = BST_Node(key, data)
                self.size += 1
            else:
                self._insert_recur(node.right, key, data)

    def insert(self, key, data):
        """ Adds this value pair to the collection """
        if self.root.key == None:
            self.root = BST_Node(key, data)
            self.size += 1
        else:
            self._insert_recur(self.root, key, data)
    

    def update(self, key, data):
        """ Sets the data value of the value pair with equal key to data """
        node = self.get_node(key)
        node.data = data # LATER -- works with __setitem__ ... i think
        
    def find(self, key):
        """ Returns the data value of the value pair with equal key """
        return self.get_node(key).data
    

    def contains(self, key): # LATER looks sus - má gera TRY EXCEPT
        """ Returns True if equal key is found in the collection, otherwise False """
        try:
            self.get_node(key)
            return True
        except NotFoundException:
            return False


    def _remove_recur(self, key):
        pass
    
    def remove(self, key):
        """ Removes the value pair with equal key from the collection """        
        self.size -= 1
        pass


    def __setitem__(self, key, data): # LATER looks sus - má gera TRY EXCEPT
        """ Override to allow this syntax: some_bst_map[key] = data.
         If equal key is already in the collection, update its data value """
        try:
            self.insert(key, data)
        except ItemExistsException:
            self.update(key, data)

    def __getitem__(self, key):
        """ Returns the data value of the value pair with equal key """
        # TA -- er þetta bara nákvæmlega það sama og find -- nema bara með bandstriks dæminu
        return self.get_node(key).data

    def __len__(self):
        """ Returns the number of items in the entire data structure """
        return self.size


    def _inorder_recur(self, node, ret="output:"):
        if node:
            ret = self._inorder_recur(node.left, ret)
            ret += f" {{{node.key}:{node.data}}}"
            ret = self._inorder_recur(node.right, ret)
        return ret

    def __str__(self): # TA is the format correct :  output: {1:one} {2:two} etc?
        """ Returns a string with the items ordered by key and separated by a single space """
        return self._inorder_recur(self.root) if self.root.data else ""

    

    def _get_node_recur(self, node, key): # JB helper func? itl að minnka duplicate code
        """ Returns the node of the value pair with equal key """
        if node.key == key:
            return node
        
        if key < node.key:
            if node.left:
                return self._get_node_recur(node.left, key)
        elif key > node.key:
            if node.right:
                return self._get_node_recur(node.right, key)

    def get_node(self, key):
        """ Returns the data value of the value pair with equal key """
        if self.root.data == None:
            raise NotFoundException()
        
        node = self._get_node_recur(self.root, key)
        if not node:
            raise NotFoundException()
        return node


if __name__ == "__main__":
    pass