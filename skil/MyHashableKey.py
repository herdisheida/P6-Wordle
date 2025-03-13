import random

class MyHashableKey:

    def __init__(self, int_value, str_value):
        """ A constructor that takes an integer value and a string value """
        self.int_value = int_value
        self.str_value = str_value

    def __eq__(self, other):
        """ Compares two instances of MyHashableKey and returns True if their values are equal, otherwise False """
        return (self.int_value, self.str_value) == (other.int_value, other.str_value)


# TODO -- muna að búa til hash fall :D :D :D
    def __hash__(self):
        """ Returns a positive integer """
        # hash = self.int_value
        # for x in range(len(self.str_value)):
        #     hash += ord(self.str_value[x])   
        # return hash

        random.seed(self.int_value)
        hash = random.randint()
        for x in range(len(self.str_value)):
            hash += ord(self.str_value[x]) + random.randint()
        return hash