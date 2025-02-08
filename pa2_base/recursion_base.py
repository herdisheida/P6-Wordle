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
    if head == None or head.next == None:
        return head
    # # inductive step
    # print("head: ", head)
    # print("head.next: ", head.next)
    # new_head = reverse_list(head.next)
    # print("new_head: ",new_head)
    # head.next = head
    # head = None
    print("head: ", head.data)
    print("head.next: ", head.next.data if head.next != None else 124)

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




    # planið: find the tail
    reversed = reverse_list(head.next)
    current = reversed
    while current.next:
        current = current.next
    current.next = Node(head.data)
    return reversed


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
