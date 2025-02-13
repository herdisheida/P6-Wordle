from pa2_base.recursion_base import Node, print_to_screen, reverse_list, palindrome




def palindrome_test():
    print("MY TESTS")
    print()
    head = Node("H", Node("E", Node("R", Node("D", Node("I", Node("S", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head) # check if list breaks after check
    print()
    head = Node("H", Node("E", Node("R", Node("R", Node("E", Node("H", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head) # check if list breaks after check
    head = Node("H", Node("E", Node("R", Node("E", Node("H", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head) # check if list breaks after check

if __name__ == "__main__":
    palindrome_test()