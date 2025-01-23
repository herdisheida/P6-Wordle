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
        size = 5 # HELP breyta þessu seinna - vtk hvort ég ætli að hardkóða size
        self.array = [0] * size if size else []
        self.size = size if size else 0 # len(array)


    #Time complexity: O(n) - linear time in size of list
    def __str__(self) -> str:
        """ Returns a string with all items from the array.
        Have a comma and a space between them. """
        return_string = ""
        index = 0
        self.array_length = self._get_array_length() # má þetta vera hér HELP

        while index < self.array_length - 1:

            if index != self.array_length:
                return_string += f"{self.array[index]}" + ", "
            index += 1

        # add the last element, without a comma
        return_string += f"{self.array[index]}"
        return return_string

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value) -> None:
        """ Inserts an item into the list before the first item """
        self.array = [value] + self.array # má gera þetta HELP - lookar of létt

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index: int) -> None:
        """ Inserts an item into the list at a specific location, not overwriting other items.
        If the index is not within the current list, raise IndexOutOfBounds().
        It should be possible to add to the front and back of the list, and anywhere in between """

        # the empty list
        if not self.array:
            self.array = [value]

        # adding in the front
        if index == 0:
            self.prepend(value)
        
        # adding at the back
        # if index == self._get_array_length() - 1:
        #     self.append(value)

        # adding in between
        # try:
        #     # make template for new list
        #     new_array = [0] * (self.size + 1)

        #     # insert each element into the new_array, once at a time
        #     for x in range(self.array_length): # má þetta ? EXTRA HELP TA - ég er ekki að nota for x in list, en er að nota lengdinu á listanum...
        #         # insert the new element
        #         if x == index:
        #             new_array[x] = value
        #         new_array[x] = self.array[x]

        # except :
        #     raise IndexOutOfBounds() # vtk en hvor ég negi nota try: except: HELP

    #Time complexity: O(1) - constant time
    def append(self, value) -> None:
        """ Adds an item to the list after the last item. """
        self.array += [value]


    #Time complexity: O(1) - constant time
    def set_at(self, value, index: int) -> None:
        """ Sets the value at a specific location to a specific value.
        Overwrites the current value there.
        If the index is not within the current list, raise IndexOutOfBounds(). """

        try: # má þetta HELP - lookar too easy...
            self.array[index] = value
        except :
            raise IndexOutOfBounds()


    #Time complexity: O(1) - constant time
    def get_first(self) -> int:
        """ Returns the first item in the list.
        Raises Empty() if the list is empty.
        """
        if not self.array:
            raise Empty()
        return self.array[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index: int) -> int:
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
    def remove_at(self, index: int) -> None:
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
    print(arr_lis)


    # testing - að setja eitthvað í listan, einhverstaðar
    arr_lis.prepend("prepending HERE")
    print(arr_lis)
    arr_lis.append("appending HERE")
    print(arr_lis)
    # arr_lis.set_at("set_at HERE", 1)
    # print(arr_lis)

    # arr_lis.insert("inserting HERE", 0)
    # print(arr_lis)


    # print(str(arr_lis))