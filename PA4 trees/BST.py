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


    def _insert_recur(self, node, key, data):
        if node == None:
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

    def update(self, key, data):
        """ Sets the data value of the value pair with equal key to data """
        self._get_node(key).data = data
    
    def find(self, key):
        """ Returns the data value of the value pair with equal key """
        return self._get_node(key).data
    
    def contains(self, key): # LATER looks sus - má gera TRY EXCEPT?
        """ Returns True if equal key is found in the collection, otherwise False """
        try:
            self._get_node(key)
            return True
        except NotFoundException:
            return False


    def _find_left_most(self, node, node_to_remove):
        # find leftMost node
        if node.left:
            self._find_left_most()
        return node

    def _remove_recur(self, node, key):
        if node == None:
            raise NotFoundException()

        if key < node.key:
            node.left = self._remove_recur(node.left, key)
        elif node.key < key:
            node.right = self._remove_recur(node.right, key)
        else: # node is found

            self.size -= 1
            # node has 0 children
            if not node.left and not node.right:
                return None

            # node has 1 child
            elif node.left:
                return node.left
            elif node.right:
                return node.right

            # node has 2 children
            else:
                leftMost = self._find_left_most(node.right, node)
                node.key, node.data = leftMost.key, leftMost.data
                return self._remove_recur(leftMost)
            
        return node


    def remove(self, key):
        """ Removes the value pair with equal key from the collection """        
        self._remove_recur(self.root, key)


            




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
        return self._get_node(key).data

    def __len__(self):
        """ Returns the number of items in the entire data structure """
        return self.size


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


## utilify func
    def _get_node_recur(self, node, key):
        if node == None:
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


if __name__ == "__main__":
    pass
