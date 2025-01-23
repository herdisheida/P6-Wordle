from curses import A_ALTCHARSET


class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass





# HELP EDIT LATER : skoða seinna
# HELP : basic hjálp
# EXTRA HELP TA : spyrja kennara
# HELP PA : spyrja félaga
# DELETE LATER: eyða seinna

# TODO:
# TODO: Sorting and searching (20%)


class ArrayList:
    def __init__(self) -> None:
        """ Initializes the array list """

        # Default is an empty list
        self.size = 0
        self.capacity = 3
        self.a_list = [None] * self.capacity


    #Time complexity: O(n) - linear time in size of list
    def __str__(self) -> str:
        """ Returns a string with all items from the array.
        Have a comma and a space between them. """
        return_string = ""
        for x in range(self.size):
            if x == self.size - 1:
                return_string += f"{self.a_list[x]}"
            else:
                return_string += f"{self.a_list[x]}"  + ", "
        return return_string if return_string else "The Array is empty" # HELP PA - á ég að skila tómum?


    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value) -> None:
        """ Inserts an item into the list before the first item. """
        self.insert(value, 0)


    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index: int) -> None:
        """ Inserts an item into the list at a specific location, not overwriting other items. """
        if 0 > index or index > self.size:
            raise IndexOutOfBounds()
        
        self.resize()
        # Move all elements to the right, until the index
        for x in range(self.size, index, - 1):
            self.a_list[x] = self.a_list[x - 1]
        # Add the inserted value
        self.a_list[index] = value
        self.size += 1


    #Time complexity: O(1) - constant time
    def append(self, value) -> None:
        """ Adds an item to the list after the last item. """
        self.resize() # Resize the list
        self.a_list[self.size] = value # Add the new element
        self.size += 1


    #Time complexity: O(1) - constant time
    def set_at(self, value, index: int) -> None:
        """ Sets the value at a specific location to a specific value.
        Overwrites the current value there."""
        if 0 > index or index >= self.size:
            raise IndexOutOfBounds()
        self.a_list[index] = value


    #Time complexity: O(1) - constant time
    def get_first(self) -> int:
        """ Returns the first item in the list.
        Raises Empty() if the list is empty.
        """
        if self.size == 0:
            raise Empty()
        return self.a_list[0]
    

    #Time complexity: O(1) - constant time
    def get_at(self, index: int) -> int:
        """ Returns the item at index. """
        if index < 0 or index >= self.size or self.size == 0:
            raise IndexOutOfBounds()
        return self.a_list[index]


    #Time complexity: O(1) - constant time
    def get_last(self) -> int:
        """ Returns the last item in the list. """
        if self.size == 0:
            raise Empty()
        return self.a_list[self.size - 1]


    #Time complexity: O(n) - linear time in size of list
    def resize(self) -> None:
        """ Re-allocates memory for a larger array and populates it with the original array's items. """
        if self.size == self.capacity:
            self.capacity *= 2
            temp = [None] * self.capacity

            for x in range(self.size):
                temp[x] = self.a_list[x]
            self.a_list = temp


    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index: int) -> None:
        """ Removes from the list an item at a specific location. """
        if 0 > index or index >= self.size:
            raise IndexOutOfBounds()
        
        # Move all elements to the the left (overwriting the index)
        for x in range(index, self.size - 1):
            self.a_list[x] = self.a_list[x + 1]
        self.size -= 1


    #Time complexity: O(1) - constant time
    def clear(self) -> None:
        """ Removes  all items from the list. """
        self.size = 0


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





if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()

    print("\n   ALL CLEARED: ")
    arr_lis.clear()
    print("Size:      ", arr_lis.size)
    print("Capacity:  ", arr_lis.capacity)
    print("Array:     ", arr_lis, "\n")

    
        
    # TEST: add to list
    arr_lis.append("append 1 HERE")
    print(arr_lis)

    arr_lis.prepend("prepend 1 HERE")
    print(arr_lis)

    arr_lis.append("append 2 HERE")
    print(arr_lis)
    # arr_lis.prepend("prepend 2 HERE")
    # print(arr_lis)

    arr_lis.insert("insert at 0", 0)
    print(arr_lis)
    arr_lis.insert("insert at 3", 3)
    print(arr_lis)
    arr_lis.set_at("set at 0", 0)
    print(arr_lis)



    # TEST: get elements
    # x = arr_lis.get_first()
    # print(x)
    # x = arr_lis.get_at(0)
    # print(x)
    # x = arr_lis.get_last()
    # print(x)

    # TEST: remove
    arr_lis.remove_at(0)
    print("remove at 0: ", arr_lis)



    print("\n   ALL CLEARED: ")
    arr_lis.clear()
    print("Size:      ", arr_lis.size)
    print("Capacity:  ", arr_lis.capacity)
    print("Array:     ", arr_lis, "\n")

    arr_lis.insert(124, 0)
    print(arr_lis)



    arr_lis.set_at("set_at HERE", 0)
    print(arr_lis)

    arr_lis.insert("inserting HERE", 0)
    print(arr_lis)


    # print(str(arr_lis))







#     print(f""" AFTER PREPENDING
                  
# self.size = {self.size}
# self.a_list = {self.a_list}

# """)