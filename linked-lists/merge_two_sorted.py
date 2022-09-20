from node import Node, stringify_list





def mergeTwoLists(list1, list2):

    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val < list2.val:
        main = list1
        other = list2
    else:
        main = list2
        other = list1

    current = main

    while current.next and other:
        # print(f"looping. current: {current.next.val}, other: {other.val}")
        if other.val <= current.next.val:
            print(f"other smaller. {other.val}")
            temp = current.next
            current.next = other
            other = other.next
            current.next.next = temp
        print(f"main: {stringify_list(main)}")
        print(f"other: {stringify_list(other)}")
        if current.next:
            current = current.next
        
    if other:
        current.next = other


    return main







list1_3 = Node(6)
list1_2 = Node(4, list1_3)
list1_1 = Node(1, list1_2)

list2_3 = Node(5)
list2_2 = Node(4, list2_3)
list2_1 = Node(2, list2_2)

print(stringify_list(list1_1))
print(stringify_list(list2_1))

print(stringify_list(mergeTwoLists(list2_1, list1_1)))