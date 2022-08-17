from node import Node, LinkedList




def rotate(list, n):

    curr = list.head
    length = 0

    while curr is not None:
        curr = curr.next
        length += 1

    n = n % length
