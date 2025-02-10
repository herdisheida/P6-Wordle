class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def print_to_screen(head):
    if head != None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")

def get_size(head):
    # base case
    if head == None:
        return 0
    # inductive step
    return 1 + get_size(head.next)

def reverse_list(head):
    # base case
    # if head == None or head.next == None:
        # return head
    # # inductive step
    # print("head: ", head)
    # print("head.next: ", head.next)
    # new_head = reverse_list(head.next)
    # print("new_head: ",new_head)
    # head.next = head
    # head = None
    # print("head: ", head.data)
    # print("head.next: ", head.next.data if head.next != None else 124)

    # LOOP forever
    # new_head = Node(head.next, head)
    # return reverse_list(new_head)


    # test ----- GET THE SAME AS LIST...
    # node = reverse_list(head.next)
    # return Node(head.data, node)

    # node = reverse_list(head.next)
    # print("node: ", node)
    # if node == None or node.next == None or node.next.next == None:
    #     return head
    # return Node(node.data, node.next)

    # node = reverse_list(head.next)
    # print("node: ", node)
    # if head == None or node == None or node.next == None or node.next.next == None:
    #     return head
    # return Node(node.next.data, node)

    # node = reverse_list(head.next)
    # print("node: ", node)
    # if head == None or node == None:
    #     return head
    # return Node(node.data, node)


    # the front due is correct, otherwise not
    # node = reverse_list(head.next)
    # if node == None:
    #     return head
    # return Node(node.data, head)

    # node = Node(head.next, head)
    # if node == None:
    #     return head
    # return reverse_list(node)

    # not working
    # node = reverse_list(head.next)
    # if node == None:
    #     return head
    # return Node(node, head.next)




    # WORKS but is time is not good :((
    # reversed = reverse_list(head.next)
    # current = reversed
    # while current.next:
    #     current = current.next
    # current.next = Node(head.data)
    # return reversed



    # def reverse_inner(head, reversed=None):
    #     if head == None:
    #         return reversed
    #     if head.next == None:
    #         head.next = reversed
    #         return head
        
    # if head == None or head.next == None:
    #     return head
    
    # print("before", head.data)
    # reverse_list(head.next)
    # print("after:", head.data)
    # # print()
    # # node = Node(head.data, head)
    # # print("NODE: ", node.data)

    # def reverse_inner(head, tail=None):
    #     # base case
    #     if head == None or head.next == None:
    #         return head
    #     if tail == None:
    #         return 
        
    #     # inductive step
    #     new_head = Node(head.next.data, head.next.next)
    #     new_tail = Node(head.data, head.next)
    #     return reverse_inner(new_head, new_tail)


    # return reverse_inner(head)
        



    def reverse_inner(node):
        # base case
        if not node:
            return None, None # head = tail = None
        if not node.next:
            head = tail = Node(node.data)
            return head, tail
        
        # inductive step
        rev_head, rev_tail = reverse_inner(node.next) # {rev_head, ..., rev_tail}
        rev_tail.next = Node(node.data) # {rev_head, ..., rev_tail, rev_tail.next}
        return rev_head, rev_tail.next # {returning new_head, ...,  new_tail}
    
    new_head, x = reverse_inner(head)
    return new_head



def palindrome(head):
    return True

if __name__ == "__main__":
    ##
    print("GET_SIZE TESTS")
    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = None
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = Node("A", None)
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = Node("A", Node("C", None))
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)


    ##
    print("REVERSE TESTS")
    print("\n")
    head = Node("A", Node("B", Node("C", Node("D", Node("E", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("A", Node("A", Node("A", Node("B", Node("A", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", Node("B", Node("A", Node("B", Node("A", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", None)
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = None
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", Node("B", None))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)


    ##
    print("PALINDROME TESTS")
    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("A", Node("E", Node("L", Node("B", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("L", Node("A", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("T", Node("E", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")
