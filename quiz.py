class Node:

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
def print_list(head):
    if head != None:
        print(head.data, end= " ")
        print_list(head.next)
    else:
        print("")

#Example program:
head = Node("A", Node("B", Node("C", Node("D", None))))
print_list(head)
# output: A B C D

node = head
if node != None:
    while node.next != None:
        node = node.next
node.next = head
head = head.next
node.next.next = None
print_list(head)

tail = Node("D", None)
head = Node("A", Node("B", Node("C", tail)))
node = head
head = tail
tail = node
print_list(head)

tail = Node("D", None)
head = Node("A", Node("B", Node("C", tail)))
node = head
head = tail
tail = node
head.next = tail.next
tail.next = None
print_list(head)