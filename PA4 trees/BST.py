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
        self.root = None
        self.size = 0

## ------------ INSERT ------------ ##
    def _insert_recur(self, node, key, data):
        if node is None:
            return BST_Node(key, data)

        if key < node.key:
            node.left = self._insert_recur(node.left, key, data)
        elif node.key < key:
            node.right = self._insert_recur(node.right, key, data)
        else: # node is found
            raise ItemExistsException()
        return node

    def insert(self, key, data):
        """ Adds this value pair to the collection """
        self.root = self._insert_recur(self.root, key, data)
        self.size += 1

## ------------ UPDATE ------------ ##
    def update(self, key, data):
        """ Sets the data value of the value pair with equal key to data """
        self._get_node(key).data = data

## ------------ FIND ------------ ##
    def find(self, key):
        """ Returns the data value of the value pair with equal key """
        return self._get_node(key).data
    
## ------------ CONSTAIN ------------ ##
    def contains(self, key):
        """ Returns True if equal key is found in the collection, otherwise False """
        try:
            self._get_node(key)
            return True
        except NotFoundException:
            return False
        
## ------------ CONSTAIN ------------ ##
    def _find_left_most(self, node):
        # find leftMost node
        if node.left:
            return self._find_left_most(node.left)
        return node

## ------------ REMOVE ------------ ##
    def _remove_recur(self, node, key):
        if node is None:
            raise NotFoundException()
        if key < node.key:
            node.left = self._remove_recur(node.left, key)
        elif key > node.key:
            node.right = self._remove_recur(node.right, key)
        else: # node is found

            # node has 1 child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # node has 2 children  
            left_most_node = self._find_left_most(node.right)
            node.key, node.data = left_most_node.key, left_most_node.data
            node.right = self._remove_recur(node.right, left_most_node.key)
        return node

    def remove(self, key):
        """ Removes the value pair with equal key from the collection """    
        self.root = self._remove_recur(self.root, key)
        self.size -= 1

## ------------ SET ITEM ------------ ##
    def __setitem__(self, key, data):
        """ Override to allow this syntax: some_bst_map[key] = data.
         If equal key is already in the collection, update its data value """
        try:
            self.insert(key, data)
        except ItemExistsException:
            self.update(key, data)

## ------------ GET ITEM ------------ ##
    def __getitem__(self, key):
        """ Returns the data value of the value pair with equal key """
        return self._get_node(key).data

## ------------ LEN ------------ ##
    def __len__(self):
        """ Returns the number of items in the entire data structure """
        return self.size

## ------------ PRINT ------------ ##
    def _inorder_recur(self, node, ret="output:"):
        if node:
            ret = self._inorder_recur(node.left, ret)
            ret += f" {{{node.key}:{node.data}}}"
            ret = self._inorder_recur(node.right, ret)
        return ret

    def __str__(self):
        """ Returns a string with the items ordered by key and separated by a single space.
         Format: {value_of_key:value_of_data} """
        return self._inorder_recur(self.root) if self.root else ""

## ------------ GET NODE helper func ------------ ##
    def _get_node_recur(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node
        elif key < node.key:
            return self._get_node_recur(node.left, key)
        else: # key > node.key:
            return self._get_node_recur(node.right, key)
        
    def _get_node(self, key):
        """ Returns the data value of the value pair with equal key """
        node = self._get_node_recur(self.root, key)
        if not node:
            raise NotFoundException()
        return node
## ------------------------------ ##


if __name__ == "__main__":
    pass
