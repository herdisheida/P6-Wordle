class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass


class ArrayList:
    def __init__(self, size: int = None) -> None:
        """ Initializes the array list """
        size = 4 # HELP
        self.array = [0] * size if size else []
        self.size = size if size else 0 # len(array)

    #Time complexity: O(n) - linear time in size of list
    def __str__(self) -> str:
        """ Returns a string with all items from the array.
        Have a comma and a space between them. """
        return_string = ""
        index = 0
        array_length = self._get_array_length()

        while index < array_length - 1:

            if index != array_length:
                return_string += f"{self.array[index]}" + ", "
            index += 1

        # add the last element, without a comma
        return_string += f"{self.array[index]}"
        return return_string

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value) -> None:
        """ Inserts an item into the list before the first item """

        new_array = [0] + self.array # má gera þetta HELP
        new_array[0] = value
        self.array = new_array

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index) -> None:
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def append(self, value) -> None:
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def set_at(self, value, index) -> None:
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_first(self) -> int:
        """ Returns the first item in the list.
        Raises Empty() if the list is empty.
        """
        if not self.array:
            raise Empty()
        return self.array[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index) -> int:
        """ Returns the item at index.
        Raises IndexOutOfBounds() if index is invalid. """

        # # List is empty
        # if not self.array():
        #     raise IndexOutOfBounds()

        # # Index is a negative num
        # if index < 0:
        #     raise IndexOutOfBounds()
        
        # HELP - má ég bara gera þetta
        try:
            return self.array[index]
        except :
            raise IndexOutOfBounds()         
        

         

    #Time complexity: O(1) - constant time
    def get_last(self) -> int:
        """ Returns the last item in the list.
        Raises Empty() if the list is empty. """
        # how do i do this if i'm not allowed to use list[-a] ? - spyrja TA
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def resize(self) -> None:
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index) -> None:
        """ Removes from the list an item at a specific location.
        If the index is not within the current list, raise IndexOutOfBounds(). """
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def clear(self) -> None:
        """ Removes  all items from the list. """
        self.array = []
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value) -> None:
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value) -> int:
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value) -> None:
        # TODO: remove 'pass' and implement functionality
        pass



    def _get_array_length(self, index=0) -> int:
        """ Get the length of the array """

        # # the empty list
        # if not self.array:
        #     return 0
        
        try:
            value_at_index = self.array[index]
            return self._get_array_length(index + 1)
        except IndexError:
            # stop calling recoursively, when index gets out of range
            return index




if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()

    # test
    arr_lis.prepend("HEllo World")


    print(str(arr_lis))