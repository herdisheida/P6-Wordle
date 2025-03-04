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
        if key < node.key:
            if node.left == None:
                node.left = BST_Node(key, data)
                self.size += 1
            else:
                self._insert_recur(node.left, key, data)
        elif node.key < key:
            if node.right == None:
                node.right = BST_Node(key, data)
                self.size += 1
            else:
                self._insert_recur(node.right, key, data)
        else: # key == node.key
            raise ItemExistsException()

    def insert(self, key, data):
        """ Adds this value pair to the collection """
        if self.root.key == None:
            self.root = BST_Node(key, data)
            self.size += 1
        else:
            self._insert_recur(self.root, key, data)
            




# LATER trying to refactor
    # def _insert_recur(self, node, key, data):

    #     if node == None:
    #         new_node = BST_Node(key, data)
    #         if self.root.key == None:
    #             self.root = new_node
    #         node = new_node
    #         self.size += 1
    #         return
        
    #     if key < node.key:
    #         # if node.left == None:
    #         #     node.left = BST_Node(key, data)
    #         #     self.size += 1
    #         # else:
    #         self._insert_recur(node.left, key, data)
    #     elif node.key < key:
    #         # if node.right == None:
    #         #     node.right = BST_Node(key, data)
    #         #     self.size += 1
    #         # else:
    #         self._insert_recur(node.right, key, data)
    #     else:
    #         raise ItemExistsException()

    # def insert(self, key, data):
    #     """ Adds this value pair to the collection """
    #     # if self.root.key == None:
    #     #     self.root = BST_Node(key, data)
    #     #     self.size += 1
    #     # else:
    #     self._insert_recur(self.root, key, data)


# kári
    # def _insert_recur(self, node, key, data):
    #     if node == None:
    #         return BST_Node(key, data)

    #     if key < node.key:
    #         self._insert_recur(node.left, key, data)
    #     elif node.key < key:
    #         self._insert_recur(node.right, key, data)
    #     else: # key == node.key
    #         raise ItemExistsException()
    #     return node

    # def insert(self, key, data):
    #     """ Adds this value pair to the collection """
    #     if self.root.key == None:
    #         self.root = BST_Node(key, data)
    #     else:
    #         node = self._insert_recur(self.root, key, data)
    #     self.size += 1




    def update(self, key, data):
        """ Sets the data value of the value pair with equal key to data """
        self.get_node(key).data = data
        
    def find(self, key):
        """ Returns the data value of the value pair with equal key """
        return self.get_node(key).data
    
    def contains(self, key): # LATER looks sus - má gera TRY EXCEPT?
        """ Returns True if equal key is found in the collection, otherwise False """
        try:
            self.get_node(key)
            return True
        except NotFoundException:
            return False


    def _remove_recur(self, node, key):
        if node.left:
            if node.left.key == key:
                node.left = node.left.left
                node.right = node.left.right
        if node.right:
            if node.right.key == key:
                node.right = node.right.right
                node.left = node.right.left

        if key < node.key:
            if node.left:
                self._remove_recur(node.left, key)
        elif key > node.key:
            if node.right:
                self._remove_recur(node.right, key)
    
    def remove(self, key):
        """ Removes the value pair with equal key from the collection """        
        if self.size == None:
            raise NotFoundException()
        
        if self.root.key == key:
            pass # HELP can we remove root?
            
        
        self._remove_recur(self.root, key)
        # if not node:
            # raise NotFoundException()
        self.size -= 1
        # return node


    def __setitem__(self, key, data): # LATER looks sus - má gera TRY EXCEPT?
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
        """ Returns a string with the items ordered by key and separated by a single space.
         Format: {value_of_key:value_of_data} """
        return self._inorder_recur(self.root) if self.root.data else ""


    def _get_node_recur(self, node, key): # JB helper func? itl að minnka duplicate code
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
