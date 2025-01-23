class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass


# TODO: rezise stuff,
# TODO: breyta append, prepend og insert - þarf að nota rezise þar
# TODO: eyða get_array_length - þarf ekki að nota það því ég hef self.size breytuna

# HELP EDIT LATER : skoða seinna
# HELP : basic hjálp
# EXTRA HELP TA : spyrja kennara
# HELP PA : spyrja félaga


class ArrayList:
    def __init__(self, capacity: int = 10) -> None:
        """ Initializes the array list """
        self.array = [None] * capacity # default capacity is 10

        # how manu elements the array can hold
        self.capacity = capacity if capacity else 0
        # how many elements are in the array
        self.size = 0


    #Time complexity: O(n) - linear time in size of list
    def __str__(self) -> str:
        """ Returns a string with all items from the array.
        Have a comma and a space between them. """
        return_string = ""
        index = 0

        while index < self.size - 1:

            if index != self.size:
                # add the all elements, except the last one
                return_string += f"{self.array[index]}" + ", "
            else:
                # add the last element
                return_string += f"{self.array[index]}"

            index += 1

        # return an empty string if the array is empty
        # HELP PA - á ég að skila tómum?
        return return_string if return_string else "The Array is empty"

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

        # List is empty
        if self.size == 0:
            raise IndexOutOfBounds()

        # Index is out of bounds; negatie or bigger than the size of the list
        if index < 0 or index >= self.size:
            raise IndexOutOfBounds()

        # return the element at the index
        return self.array[index]


    #Time complexity: O(1) - constant time
    def get_last(self) -> int:
        """ Returns the last item in the list.
        Raises Empty() if the list is empty. """
        # how do i do this if i'm not allowed to use list[-a] ? - spyrja TA
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def resize(self) -> None:
        """ Re-allocates memory for a larger array and populates it with the original array's items. """
        # make a new array with the size of the original array + 1
        new_array = [None] * (self.size + 1)

        # insert each element into the new_array
        for x in range(self.size):
            new_array[x] = self.array[x]

        # set the new_array as the array
        self.array = new_array


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

        # the empty list
        if not self.array:
            return 0
        
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

    arr_lis = ArrayList(5) # 5 is the size of the list - vtk á ég að hardkóða? HELP EDIT LATER
    print(arr_lis)
    print(arr_lis.array)

    arr_lis.resize()
    print(arr_lis)


    # testing - að setja eitthvað í listan, einhverstaðar
    # arr_lis.prepend("prepending HERE")
    # print(arr_lis)
    # arr_lis.append("appending HERE")
    # print(arr_lis)
    # arr_lis.set_at("set_at HERE", 1)
    # print(arr_lis)

    # arr_lis.insert("inserting HERE", 0)
    # print(arr_lis)


    # print(str(arr_lis))