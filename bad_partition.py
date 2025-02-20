
def partition(self, low, high):
    """Loops from low to high and moves all nodes smaller than low so they are ahead (left side) of the low node"""
    if low == high or self.size == 0:
        return
    

    # pivot = low
    # low_data = low.data
    # while pivot != high.next:
    #     # check if "temp" is smaller than "low"
    #     if pivot.data < low_data:

    #         temp_data = pivot.data
    #         pivot.data = low_data
    #         pivot.prev.data = temp_data

    #     pivot = pivot.next
    # self.current_pos = low
    # return self.current_pos

    
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