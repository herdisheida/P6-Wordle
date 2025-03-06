
class MyComparableKey:

    def __init__(self, int_value, string_value):
        """ A constructor that takes an integer value and a string value """
        self.key = int_value
        self.data = string_value

    def __lt__(self, other):
        """ Compares two instances of MyComparableKey and returns True if the value of self is lower, otherwise False. 
         In case of equal integers the order of the strings is used """        
        if self.key == other.key and self.data < other.data:
                return True
        if self.key < other.key:
            return True    
        return False

