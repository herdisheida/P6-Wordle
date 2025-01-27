class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass



class ArrayList:
    def __init__(self):
        """ Initializes the array list """
        self.size = 0
        self.capacity = 3
        self.a_list = [None] * self.capacity
        self.is_ordered = True


    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        """ Returns a string with all items from the list, separated by a comma and a space. """
        return_string = ""
        for x in range(self.size):
            if x == self.size - 1:
                return_string += f"{self.a_list[x]}"
            else:
                return_string += f"{self.a_list[x]}"  + ", "
        return return_string


    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        """ Inserts an item into the list before the first item. """
        self.insert(value, 0)


    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
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
        self.is_ordered = False


    #Time complexity: O(1) - constant time
    def append(self, value):
        """ Adds an item to the list after the last item. """
        self.resize()
        self.a_list[self.size] = value
        self.size += 1
        self.is_ordered = False


    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        """ Sets the value at a specific location to a specific value.
        Overwrites the current value there. """
        if 0 > index or index >= self.size:
            raise IndexOutOfBounds()
        self.a_list[index] = value
        self.is_ordered = False


    #Time complexity: O(1) - constant time
    def get_first(self):
        """ Returns the first item in the list. """
        if self.size == 0:
            raise Empty()
        return self.a_list[0]
    

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        """ Returns the item at index. """
        if index < 0 or index >= self.size or self.size == 0:
            raise IndexOutOfBounds()
        return self.a_list[index]


    #Time complexity: O(1) - constant time
    def get_last(self):
        """ Returns the last item in the list. """
        if self.size == 0:
            raise Empty()
        return self.a_list[self.size - 1]


    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        """ Re-allocates memory for a larger array and populates it with the original array's items. """
        if self.size == self.capacity:
            self.capacity *= 2
            temp = [None] * self.capacity

            for x in range(self.size):
                temp[x] = self.a_list[x]
            self.a_list = temp


    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        """ Removes from the list an item at a specific location. """
        if 0 > index or index >= self.size:
            raise IndexOutOfBounds()
        # Move all elements to the the left (overwriting the index)
        for x in range(index, self.size - 1):
            self.a_list[x] = self.a_list[x + 1]
        self.size -= 1


    #Time complexity: O(1) - constant time
    def clear(self):
        """ Removes  all items from the list. """
        self.size = 0
        self.is_ordered = True


    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
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
    def find(self, value):
        """ Returns the index of a specific value. """
        if self.is_ordered: # O(log n)
            low = 0
            high = self.size

            while low <= high:
                mid = (low + high) // 2
                if value == self.a_list[mid]:
                    return mid
                elif value < self.a_list[mid]:
                    high = mid - 1
                elif value > self.a_list[mid]:
                    low = mid + 1
        else: # O(n)
            for x in range(self.size):
                if value == self.a_list[x]:
                    return x
        raise NotFound()


    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        """ Removes from the list an item with a specific value. """
        for x in range(self.size):
            if value == self.a_list[x]:
                self.remove_at(x)
                return
        raise NotFound()





if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    print(str(arr_lis))