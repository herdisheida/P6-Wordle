
class MyComparableKey:

    def __init__(self, int_value, string_value):
        """ A constructor that takes an integer value and a string value """
        self.int_val = int_value
        self.str_val = string_value

    def __lt__(self, other):
        """ Compares two instances of MyComparableKey and returns True if the value of self is lower, otherwise False. 
         In case of equal integers the order of the strings is used """
        # HELP er þetta  allt of sumt?
        
        if self.int_val == other.int_val:
            if self.str_val < other.str_val:
                return True
        if self.int_val < other.int_val:
            return True    
        return False

