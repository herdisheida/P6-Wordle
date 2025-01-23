import re


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
# DELETE LATER: eyða seinna



# ÆTLA NOTA capacity - 

class ArrayList:
    def __init__(self) -> None:
        """ Initializes the array list """

        # default is an empty list
        self.size = 0
        self.array = [None] * self.size

    #Time complexity: O(n) - linear time in size of list
    def __str__(self) -> str:
        """ Returns a string with all items from the array.
        Have a comma and a space between them. """
        return_string = ""
        index = 0


        while index < self.size:

            if index != self.size - 1:
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

        # Resize the list
        self.resize()

        # If the list is not empty
        if self.size != 1:

            old_list = self.array # save this

            # Move all elements to the right by one
            for x in range(self.size - 1):
                self.array[x + 1] = old_list[x]

        # Set the new value as the first element
        self.array[0] = value


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

        # Resize the list
        self.resize()
        # Add the new element
        self.array[self.size - 1] = value


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

        # List is empty
        if self.size == 0:
            raise Empty()
        
        # return the last element
        return self.array[self.size - 1]

    #Time complexity: O(n) - linear time in size of list
    def resize(self) -> None:
        """ Re-allocates memory for a larger array and populates it with the original array's items. """
        
        # Increase the list by 1
        self.size += 1
        # Make template for the new list
        new_array = [None] * (self.size)

        # If the list is not empty
        if self.array:
            # Copy old elements to the template
            for x in range(self.size - 1):
                new_array[x] = self.array[x]
                
        # Save the list
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



    def _get_array_length(self, index=0) -> int: # MIGHT DELETE LATER
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

    arr_lis = ArrayList()
    print(arr_lis)

    
    

    # testing - að setja eitthvað í listan, einhverstaðar
    arr_lis.prepend("prepending 1 HERE")
    # print(arr_lis)

    arr_lis.append("appending 1 HERE")
    print(arr_lis)

    arr_lis.prepend("prepending 2 HERE")
    # print(arr_lis)

    # arr_lis.set_at("set_at HERE", 1)
    # print(arr_lis)

    # arr_lis.insert("inserting HERE", 0)
    # print(arr_lis)


    # print(str(arr_lis))







#     print(f""" AFTER PREPENDING
                  
# self.size = {self.size}
# self.array = {self.array}

# """)