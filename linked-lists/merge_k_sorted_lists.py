from node import Node, stringify_list



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mergeKLists(lists):
    if not lists:
        return None
#         takes heads of two lists, returns head of merged sorted
    def merge(list1, list2):
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
            if other.val <= current.next.val:
                temp = current.next
                current.next = other
                other = other.next
                current.next.next = temp

            if current.next:    
                current = current.next
            else:
                break
        if other:
            current.next = other
        return main        
    
    
    
    
    def merge_list(lists, l, r):
        if l >= r:
            return lists[r]
        
        mid = (l+r) // 2
        
        l_head = merge_list(lists, l, mid)
        r_head = merge_list(lists, mid+1, r)
        
        return merge(l_head, r_head)
    
    
    return merge_list(lists, 0, len(lists)-1)
    

list1_3 = Node(6)
list1_2 = Node(4, list1_3)
list1_1 = Node(1, list1_2)

list2_3 = Node(5)
list2_2 = Node(4, list2_3)
list2_1 = Node(2, list2_2)

print(stringify_list(list1_1))
print(stringify_list(list2_1))
test1 = [list1_1, list2_1]
print(stringify_list(mergeKLists(test1)))