class MyHashableKey:

    def __init__(self, int_value, str_value):
        """ A constructor that takes an integer value and a string value """
        self.int_value = int_value
        self.str_value = str_value

    def __eq__(self, other):
        """ Compares two instances of MyHashableKey and returns True if their values are equal, otherwise False """
        return self.int_value == other.int_value and self.str_value == other.str_value

    def __hash__(self):
        """ Returns a positive integer.
         The integer value must be the same for instances that are equal.
         Otherwise can be any integer """
        
        # use prime numbers [33, 17] to reduce collision (all items going to the same bucket)
        hash_value = 33

        # mix integer into the hash
        hash_value = hash_value * 17 + self.int_value  

        # mix string into the hash
        for char in self.str_value:
            hash_value = hash_value * 17 + ord(char)  # hash_value * 2^4 + ord(char)

        # ensure value is non-negative
        return hash_value & 0xFFFFFFFF