class ArrayList():

    def __str__(self):
        """
        ○ Returns a string with all items from the array
        ○ Have a comma and a space between them
        ■ but no brackets ([ ]) around them
        """
        pass

    def prepend(self, value):
        """
        Inserts an item into the list before the first item
        """
        pass


    def insert(self, value, index):
        """
        ○ Inserts an item into the list at a specific location, not overwriting other items
        ○ If the index is not within the current list, raise IndexOutOfBounds()
        ○ It should be possible to add to the front and back of the list, and anywhere in between
        """
        pass

    def append(self, value):
        """
        ○ Adds an item to the list after the last item
        """
        pass
    
    def set_at(self, value, index):
        """○ Sets the value at a specific location to a specific value
        ■ Overwrites the current value there
        ■ If the index is not within the current list, raise IndexOutOfBounds()
        """
    pass

    def get_first(self):
        """○ Returns the first value in the list
        ○ If there are no items in the list, raise Empty()
        """
        pass
    
    def get_at(self, index):
        """
        ○ Returns the value at a specific location in the list
        ○ If the index is not within the current list, raise IndexOutOfBounds()
        """
        pass

    def get_last(self):
        """
        ○ Returns the last value in the list
        ○ If there are no items in the list, raise Empty()
        """
        pass

    def resize(self):
        """
        ○ Re-allocates memory for a larger array and populates it with the original array’s items
        """

    def remove_at(self, index):
        """
        ○ Removes from the list an item at a specific location
        ○ If the index is not within the current list, raise IndexOutOfBounds()
        """
        pass
        
    def clear(self):
        """
        ○ Removes all items from the list
        """
        pass