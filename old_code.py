# class bucket remove()

def remove(self, key):
    """Removes the value pair with equal key from the collection"""
    temp_head = Node(None, None, self.head)
    prev, curr = temp_head, temp_head.next

    while curr:
        if curr.key == key:
            prev.next = curr.next
            self.head = temp_head.next
            self.size -= 1
            return
        prev, curr = curr, curr.next
    raise NotFoundException()





# __str__ fall er ekki í verkefnalýsingunni (geyma hér)

def __str__(self):
    """testing BUCKET str"""
    return_str = ""
    current = self.head
    while current:
        return_str += f"{{{current.key}:{current.data}}} "
        current = current.next
    return return_str

def __str__(self):
    """testing HASH MAP str"""
    # DELETE - þessi klasi hefur ekki __str__ func
    ret = ""
    for x in self.bucket_list:
        ret += str(x)
    return ret
