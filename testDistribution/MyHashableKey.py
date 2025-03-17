import random

class MyHashableKey:

    def __init__(self, int_value, str_value):
        """ A constructor that takes an integer value and a string value """
        self.int_value = int_value
        self.str_value = str_value

    def __eq__(self, other):
        """ Compares two instances of MyHashableKey and returns True if their values are equal, otherwise False """
        return self.int_value == other.int_value and self.str_value == other.str_value


# TODO -- muna að búa til hash fall :D :D :D
    def __hash__(self):
        """ Returns a positive integer """
        # hash = self.int_value
        # for x in range(len(self.str_value)):
        #     hash += ord(self.str_value[x])   
        # return hash



        # random.seed(self.int_value)
        # hashed_value = random.randint(0, self.int_value)

        # for digit in str(self.int_value):
        #     hashed_value *= ord(digit)

        # for char in self.str_value:
        #     hashed_value *= ord(char)

        # return hashed_value


        # return hash((self.int_value, self.str_value))
        



        # use prime numbers to reduce collision 
        hash_value = 33

        # mix integer into the hash
        hash_value += (hash_value * 17) + self.int_value  # hash_value * 2^4 + int_value

        # mix string into the hash
        for char in self.str_value:
            hash_value += (hash_value * 17) + ord(char)  # hash_value * 2^4 + ord(char)

        # ensure value is non-negative
        return hash_value & 0xFFFFFFFF