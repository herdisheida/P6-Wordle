# class bucket remove()

def remove(self, key):
    """Removes the value pair with equal key from the collection"""
    if self.head == None:
        raise NotFoundException()

    if self.head.key == key:
        self.head = self.head.next
        self.size -= 1
        return

    curr = self.head
    while curr.next:
        if curr.next.key == key:
            curr.next = curr.next.next
            self.size -= 1
            return
        curr = curr.next
    raise NotFoundException()