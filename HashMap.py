class Bucket:

    def __init__(self):
        """Initializes the bucket."""
        pass

    def insert(self, key, data):
        """Adds this value pair to the collection."""
        pass

    def update(self, key, data):
        """Sets the data value of the value pair with equal key to data."""
        pass

    def find(self, key):
        """Returns the data value of the value pair with equal key."""
        pass

    def contains(self, key):
        """Returns True if equal key is found in the collection, otherwise False."""
        pass

    def remove(self, key):
        """Removes the value pair with equal key from the collection."""
        pass

    def __setitem__(self, key, data):
        """Override to allow this syntax: some_hash_map[key] = data."""
        pass

    def __getitem__(self, key):
        """Override to allow this syntax: my_data = some_bucket[key]."""
        pass

    def __len__(self):
        """Override to allow this syntax: length_of_structure = len(some_bucket)."""
        pass


class HashMap:

    def _init():
        pass

    def insert(self, key, data):
        """Adds this value pair to the collection."""
        pass

    def update(self, key, data):
        """Sets the data value of the value pair with equal key to data"""
        pass

    def find(self, key):
        """Returns the data value of the value pair with equal key."""
        pass

    def contains(self, key):
        """Returns True if equal key is found in the collection, otherwise False."""
        pass

    def remove(self, key):
        """Removes the value pair with equal key from the collection."""
        pass

    def __setitem__(self, key, data):
        """Override to allow this syntax: some_hash_map[key] = data."""
        pass

    def __getitem__(self, key):
        """Override to allow this syntax: my_data = some_hash_map[key"""
        pass

    def __len__(self):
        """Override to allow this syntax: length_of_structure = len(some_hash_map)."""
        pass

class MyHashableKey:

    def __init__(self):
        pass

    def __eq__(self, other):
        """Compares two instances of MyHashableKey and returns True if their values are equal, otherwise False."""
        pass

    def __hash__(self):
        """Returns a positive integer."""
        pass