from operator import is_
from re import S
import re


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


# HELP IS THIS OKEY : á ég að hafa þetta


# TODO: Base implementation (60%)
# TODO: Sorting and searching (20%)
# TODO: Recursion (20%)


# TODO: fix is_ordered check (variable) : when insert() is called the is_ordered should be set to False, but i can't do that because i call the insert() function in insert_ordered() function
# SPYRJA JB

class ArrayList:
    def __init__(self) -> None:
        """ Initializes the array list """

        # Default is an empty list
        self.size = 0
        self.capacity = 3
        self.a_list = [None] * self.capacity
        self.is_ordered = True


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
        # Move all elements to the right, until the index
        self.resize()
        for x in range(self.size, index, - 1):
            self.a_list[x] = self.a_list[x - 1]

        # Add the inserted value
        self.a_list[index] = value
        self.size += 1
        if self.size != 1: # HELP IS THIS OKAY -- því þetta er ekki instert_ordered
            self.is_ordered = False


    #Time complexity: O(1) - constant time
    def append(self, value) -> None:
        """ Adds an item to the list after the last item. """
        self.resize() # Resize the list
        self.a_list[self.size] = value # Add the new element
        self.size += 1
        self.is_ordered = False # EXTRA HELP PA : er þetta allt of sumt ?



    #Time complexity: O(1) - constant time
    def set_at(self, value, index: int) -> None:
        """ Sets the value at a specific location to a specific value.
        Overwrites the current value there."""
        if 0 > index or index >= self.size:
            raise IndexOutOfBounds()
        self.a_list[index] = value
        self.is_ordered = False # EXTRA HELP PA : er þetta allt of sumt ?



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

        if self.size == 0 or self.size == 1: # HELP IS THIS OKAY
            self.is_ordered = True


    #Time complexity: O(1) - constant time
    def clear(self) -> None:
        """ Removes  all items from the list. """
        self.size = 0
        self.is_ordered = True # EXTRA HELP PA : er þetta allt of sumt ? --- á þetta að vera hér?


    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value) -> None:
        """ Insert a value so that the list retains ordering. """
        if not self.is_ordered:
            raise NotOrdered()
        
        for x in range(self.size):
            if self.a_list[x] > value:
                self.insert(value, x)
                self.is_ordered = True
                return

        self.append(value)
        self.is_ordered = True


    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value) -> int:
        """ Returns the index of a specific value """

        if self.is_ordered: # O(log n)
            low = 0
            high = self.size - 1
            while low <= high:
                mid = (low + high) // 2
                
                if self.a_list[mid] == value:
                    return mid
                elif value < self.a_list[mid]:
                    high = mid - 1
                elif value > self.a_list[mid]:
                    low = mid + 1

            print("HELLO NOT FOUND")
        
        else: # O(n)
            print("for O(n)")

        raise NotFound() # if the value is not found


    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value) -> None:
        # TODO: remove 'pass' and implement functionality
        pass

        if self.size == 0 or self.size == 1: # HELP IS THIS OKAY
            self.is_ordered = True



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



    # print("\n   ALL CLEARED: ")
    # arr_lis.clear()
    # print("Size:      ", arr_lis.size)
    # print("Capacity:  ", arr_lis.capacity)
    # print("Array:     ", arr_lis, "\n")

    arr_lis1 = ArrayList()
    arr_lis1.insert(124, 0)
    print(arr_lis1)
    arr_lis1.insert(256, 1)
    print(arr_lis1)



    # TEST : insert_ordered
    arr_lis1.clear() # to test insert_ordered

    arr_lis1.insert_ordered(10)
    print(arr_lis1)
    arr_lis1.insert_ordered(562)
    print(arr_lis1)
    arr_lis1.insert_ordered(200)
    print(arr_lis1)
    arr_lis1.insert_ordered(200)
    print(arr_lis1)
    arr_lis1.insert_ordered(300)
    print(arr_lis1)
    arr_lis1.insert_ordered(600)
    print(arr_lis1)
    arr_lis1.insert_ordered(800)
    print(arr_lis1)

    assert arr_lis1.is_ordered == True

    print(arr_lis1.find(10)) # 0
    print(arr_lis1.find(200)) # 1
    print(arr_lis1.find(300)) # 3
    print(arr_lis1.find(562)) # 4
    print(arr_lis1.find(600)) # 5
    print(arr_lis1.find(800)) # 6




#     print(f""" AFTER PREPENDING
                  
# self.size = {self.size}
# self.a_list = {self.a_list}

# """)