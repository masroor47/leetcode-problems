from node import ListNode

item4 = ListNode(4)
item3 = ListNode(3, item4)
item2 = ListNode(2, item3)
head = ListNode(1, item2)

def printList(head):
    current = head
    s = ""
    while current:
        s += str(current.val) + " "
        current = current.next

    return s

print(printList(head))








def swapPairs(head):
    if head is None:
        return None
    if head.next is None:
        return head
    
    prev = head
    current = prev.next
    head = current
    print(prev.val, current.val)
    
    while current:
        # print("Swapping {} and {}".format(prev.val, current.val))
        temp = current.next
        current.next = prev
        prev.next = temp

        print("list after swap: " + printList(current))
        
        
        prev = prev.next
        if prev:
            current = prev.next
        
    
    return head


print(printList(swapPairs(head)))