from node import Node

# Comment it before submitting
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next


def Reverse(head: Node, left: int, right: int) -> Node:
    prev_start, start = None, head

    i = 1
    while i < left:
        prev_start, start = start, start.next
        i += 1

    first, second, third = (
        start,
        start.next,
        start.next.next if start.next else None,
    )

    while i < right:
        second.next = first
        first, second, third = second, third, third.next if third else None

        i += 1

    start.next = second
    if prev_start:
        prev_start.next = first
    else:
        head = first

    return head


# def print_list(head):

#     results = []
#     while head != None:
#         results.append(head.value)
#         head = head.next
#     print(" ".join(map(str, results)))


# a5 = Node(5)
# a4 = Node(4, a5)
# a3 = Node(3, a4)
# a2 = Node(2, a3)
# a1 = Node(1, a2)

# print_list(a1)

# a1 = Reverse(a1, 2, 4)
# print_list(a1)
