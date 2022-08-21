class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

class LinkedList:
    def __init__(self, node=None):
        self.head = node
    
    def insert_beginning(self, node):
        node.next = self.head
        self.head = node

    def __str__(self):
        curr = self.head
        result = "List: "
        while curr is not None:
            result += str(curr.val) + " "
            curr = curr.next

        return result

