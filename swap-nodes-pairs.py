from node import ListNode

item7 = ListNode(7)
item6 = ListNode(6, item7)
item5 = ListNode(5, item6)
item4 = ListNode(4, item5)
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


# ====== Works, but slow. Recursive might be better. ======
def swapPairs(head):
    if head is None:
        return None
    if head.next is None:
        return head
    
    prev = head
    current = prev.next
    head = current

    if current.next is None:
        current.next = prev
        prev.next = None
        return head

    while current:
        # print("Swapping {} and {}".format(prev.val, current.val))
        if current.next:
            temp = current.next
            current.next = prev
            if temp.next:
                prev.next = temp.next
            else:
                prev.next = temp
        else:
            print("hit the end so to speak")
            current.next = prev
            prev.next = None

        print(f"prev: {prev}, current: {current} after relinking")
        print("list after relinking: " + printList(head))
        
        prev = temp
        current = temp.next
    
        print(f"prev: {prev}, current: {current} after advancing")
        print("\n")
    return head


print(printList(swapPairs(head)))
