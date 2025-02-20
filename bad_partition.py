# doesnt' work either
def partition(self, low, high):
    """Loops from low to high and moves all nodes smaller than low so they are ahead (left side) of the low node"""
    if self.size == 0: # empty array
        return
    if low == high: # 1 node in array
        self.current_pos = low
        return

    pivot = low
    temp = pivot.next
    while temp != self.tail:
        # check if "temp" is smaller than "pivot"
        if temp.data < pivot.data:

            pivot_data = pivot.data # geyma

            pivot.data = temp.data
            temp.data = pivot.next.data
            pivot.next.data = pivot_data

            pivot = pivot.next
        else:
            temp = temp.next
    self.current_pos = pivot



# doesn't work for strong test in sort()
def partition(self, low, high):
    """Loops from low to high and moves all nodes smaller than low so they are ahead (left side) of the low node"""
    if self.size == 0: # empty array
        return
    if low == high: # 1 node in array
        self.current_pos = low
        return

    pivot = low
    temp = pivot.next
    
    while temp != high.next:
        # check if "temp" is smaller than "pivot"
        if temp.data < pivot.data:
            # move the temp node in front of pivot
            self.current_pos = pivot
            self.insert(temp.data)
            # severe the temp node from the original position
            self.current_pos = temp
            self.remove()
        temp = temp.next
    self.current_pos = pivot


# wrong names low is pivot or smth
def partition(self, low, high):
    """Loops from low to high and moves all nodes smaller than low so they are ahead (left side) of the low node"""
    if low == high or self.size == 0:
        return
    
    temp = low
    while temp != high.next:
        # check if "temp" is smaller than "low"
        if temp.data < low.data:
            # put the temp node to in front of "low"
            self.current_pos = low
            self.insert(temp.data)
            # severe the temp node from the original position
            self.current_pos = temp
            self.remove()
        temp = temp.next
    self.current_pos = low
    return self.current_pos





# ---------------------------------------------------------------------- #


def partition(self, low, high):
    pivot = low.data
    i = low.prev  # Tracks the last node ≤ pivot
    j = low.next   # Scans the segment

    while j != high.next:
        if j.data < pivot:
            i = i.next if i != low.prev else low
            # Swap i.data and j.data
            i.data, j.data = j.data, i.data
        j = j.next

    # Place pivot in correct position
    i = i.next if i != low.prev else low
    low.data, i.data = i.data, low.data
    return i  # Return new pivot position


def partition(self, low, high):
    pivot = low.data
    i = low.prev
    j = low

    while j != high.next:
        if j.data < pivot:
            i = i.next if i != low.prev else low
            # Swap i and j data
            i.data, j.data = j.data, i.data
        j = j.next

    # Swap i and low data to place pivot correctly
    i.data, low.data = low.data, i.data
    return i  # Return the pivot's final position

def partition(self, low, high):
    # Guard against invalid calls
    if not low or not high or low == high:
        return low  # No partitioning needed

    pivot = low.data
    i = low.prev
    j = low

    while j != high.next:
        if j.data < pivot:
            i = i.next if i != low.prev else low
            i.data, j.data = j.data, i.data
        j = j.next

    # Final swap to place pivot correctly
    i.data, low.data = low.data, i.data
    return i






#       
    def partition(self, low, high):
        """Loops from low to high and moves all nodes smaller than low so they are ahead (left side) of the low node"""
        if self.size == 0: # empty array
            return
        if low == high: # 1 node in array
            self.current_pos = low
            return
        
        pivot = low.data
        pivot_pos = low.prev # keeps track of pivot pos (all nodes left of pivot are smaller than pivot)
        temp = low.next # scans through the array (low to high)

        while temp != high.next:
            if temp.data < pivot:
                # set pivot_pos
                pivot_pos = pivot_pos.next if (pivot_pos != low.prev) else low
                # swap pivot and temp data
                pivot_pos.data, temp.data = temp.data, pivot_pos.data
            temp = temp.next

        # find pivot placement
        pivot_pos = pivot_pos.next if (pivot_pos != low.prev) else low
        pivot_pos.data, low.data = low.data, pivot_pos.data
        self.current_pos = pivot_pos
    



def partition(self, low, high):
    """Moves nodes smaller than 'low' before it, preserving node identities."""
    if self.size == 0 or low == high:
        return low

    pivot = low  # Pivot is the node to partition around
    original_high_next = high.next  # Save original end of the segment

    # Start from the node after the pivot
    temp = pivot.next

    # Process all nodes in the original [low.next, high] segment
    while temp != original_high_next:
        if temp.data < pivot.data:
            # Save next node to process (temp might move, so we save it now)
            next_temp = temp.next

            # --- Detach 'temp' from its current position ---
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

            # --- Insert 'temp' before the pivot ---
            pivot_prev = pivot.prev  # Node before pivot (could be head)
            pivot_prev.next = temp
            temp.prev = pivot_prev
            temp.next = pivot
            pivot.prev = temp

            # Move to the next node (saved earlier)
            temp = next_temp
        else:
            # No move needed; proceed to next node
            temp = temp.next

    # Return the pivot node (now in its correct position)
    return pivot








# THIS ONE
def partition(self, low, high):
    """Loops from low to high and moves all nodes smaller than low so they are ahead (left side) of the low node"""
    if self.size == 0: # empty array
        return
    if low == high: # 1 node in array
        self.current_pos = low
        return

    pivot = low
    temp = pivot.next
    while temp != self.tail:
        # check if "temp" is smaller than "pivot"
        if temp.data < pivot.data:

            pivot_data = pivot.data # geyma

            pivot.data = temp.data
            temp.data = pivot.next.data
            pivot.next.data = pivot_data

            pivot = pivot.next
        else:
            temp = temp.next
    self.current_pos = pivot