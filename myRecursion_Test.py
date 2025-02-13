from tkinter import E
from pa2_base.recursion_base import Node, print_to_screen, get_size,reverse_list, palindrome


EMPTY = None
A = Node("A", None)
AB = Node("A", Node("B", None))

HERDIS = Node("H", Node("E", Node("R", Node("D", Node("I", Node("S", None))))))
HELLO = Node("H", Node("E", Node("L", Node("L", Node("O", None)))))
ABBA = Node("A", Node("B", Node("B", Node("A",  None))))
ABCBA = Node("A", Node("B", Node("C", Node("B", Node("A", None)))))

ABCDEFGD = Node("A", Node("B", Node("C", Node("D", Node("E", Node("F", Node("G", Node("D", None))))))))
ABCDEFGDGFEDCBA = Node("A", Node("B", Node("C", Node("D", Node("E", Node("F", Node("G", Node("D", Node("G", Node("F", Node("E", Node("D", Node("C", Node("B", Node("A", None)))))))))))))))


NODE_LIST = [EMPTY, A, AB, HERDIS, HELLO, ABBA, ABCBA, ABCDEFGD, ABCDEFGDGFEDCBA]

def get_size_test():
    assert get_size(EMPTY) == 0
    assert get_size(A) == 1
    assert get_size(AB) == 2
    assert get_size(HERDIS) == 6
    assert get_size(HELLO) == 5
    assert get_size(ABBA) == 4
    assert get_size(ABCBA) == 5
    assert get_size(ABCDEFGD) == 8
    assert get_size(ABCDEFGDGFEDCBA) == 15

    print("All size tests passed")

def reverse_list_test():

    for node in NODE_LIST:
        if node is None:
            node_empty(node) # print empty node
            continue

        print("Original list", end=":\n ")
        print_to_screen(node)

        print("Reversed list", end=":\n ")
        rev_list = reverse_list(node)
        print_to_screen(rev_list)

        print("Reversed reversed list", end=":\n ")
        rev_rev_list = reverse_list(rev_list)
        print_to_screen(rev_rev_list)

        print()
        print("All reverse list tests passed")


def node_empty(node):
    print("Original list", end=":\n ")
    print(node)

    print("Reversed list", end=":\n ")
    rev_list = reverse_list(node)
    print(rev_list)

    print("Reversed reversed list", end=":\n ")
    rev_rev_list = reverse_list(rev_list)
    print(rev_rev_list)
    print()
        

def palindrome_test():
    print("Palindrome tests")

    # Empty Node
    print_to_screen(EMPTY)
    print(palindrome(EMPTY))
    assert palindrome(EMPTY) == True
    print_to_screen(EMPTY) # check if list breaks after check
    print()

    # A Node
    print_to_screen(A)
    print(palindrome(A))
    assert palindrome(A) == True
    print_to_screen(A) # check if list breaks after check
    print()

    # AB Node
    print_to_screen(AB)
    print(palindrome(AB))
    assert palindrome(AB) == False
    print_to_screen(AB) # check if list breaks after check
    print()

    # HERDIS Node
    print_to_screen(HERDIS)
    print(palindrome(HERDIS))
    assert palindrome(HERDIS) == False
    print_to_screen(HERDIS) # check if list breaks after check
    print()

    # HELLO Node
    print_to_screen(HELLO)
    print(palindrome(HELLO))
    assert palindrome(HELLO) == False
    print_to_screen(HELLO) # check if list breaks after check
    print()

    # ABBA Node
    print_to_screen(ABBA)
    print(palindrome(ABBA))
    assert palindrome(ABBA) == True
    print_to_screen(ABBA) # check if list breaks after check
    print()
    
    # ABCBA node
    print_to_screen(ABCBA)
    print(palindrome(ABCBA))
    assert palindrome(ABCBA) == True
    print_to_screen(ABCBA) # check if list breaks after check
    print()


    # ABCDEFGD Node
    print_to_screen(ABCDEFGD)
    print(palindrome(ABCDEFGD))
    assert palindrome(ABCDEFGD) == False
    print_to_screen(ABCDEFGD) # check if list breaks after check
    print()

    # ABCDEFGDGFEDCBA Node
    print_to_screen(ABCDEFGDGFEDCBA)
    print(palindrome(ABCDEFGDGFEDCBA))
    assert palindrome(ABCDEFGDGFEDCBA) == True
    print_to_screen(ABCDEFGDGFEDCBA) # check if list breaks after check
    print()


if __name__ == "__main__":
    get_size_test()
    palindrome_test()
    reverse_list_test()
    print("All tests passed")

