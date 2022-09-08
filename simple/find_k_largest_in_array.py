



def find_k_largest(nums: list[int], k: int) -> int:
    nums.sort()
    return nums[-k]

    # stupid ass question. it's very easy in python


    # k_items = []

    # for i in nums:
    #     is_largest = True
    #     for j in range(len(k_items)):
    #         if i < k_items[j]:
    #             k_items.insert(j, i)
    #             is_largest = False
    #             break
    #     if is_largest:
    #         k_items.append(i)
        
    #     if len(k_items) > k:
    #         k_items.pop(0)
    #     print(f"items: {k_items}, {i}")
    
    # return k_items[0]


print(find_k_largest([3,2,3,1,2,4,5,5,6], 4))