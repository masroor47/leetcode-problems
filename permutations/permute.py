from time import time




# Use iterative DFS
from math import perm


def permute(nums: list[int]) -> list[list[int]]:
    # print(f"working with: {nums}\n")

    
    # all_permutations = []
    # permutation = []
    # stack = [nums]

    # while stack:
    #     current_list = stack.pop()
    #     # print(f"stack: {stack}")
    #     print(f"current list: {current_list}")

    #     for i in range(len(current_list)):
    #         sublist = current_list[:]

    #         if len(sublist) > 1:
    #             sublist.pop(i)
    #             stack.append(sublist)

    #     if len(permutation) < 3:
    #         permutation.append(current_list[-1])
    #     else:
    #         all_permutations.append(permutation)
    #         permutation = []

    # return all_permutations

    
    if len(nums) == 1:
        # print(f"single item, returning: {nums}")
        return [nums]
    
    # if len(nums) == 2:
    #     list_permutations = []
    #     for i in range(2):
    #         copy = nums[:]
    #         copy.pop(i)
    #         # print(f"recursive call with copy: {copy}")
    #         list_permutations.append([nums[i]] + permute(copy))
    #         # print(f"list permutations after recieving call: {list_permutations}")
    #     return list_permutations

    if len(nums) > 1:
        list_permutations = []
        for i in range(len(nums)):
            copy = nums[:]
            copy.pop(i)
            # print(f"!recursive call with copy: {copy}")
            received = permute(copy)
            # print("receibed my stuff")
            for j in range(len(received)):
                received[j] = [nums[i]] + received[j]
            list_permutations += received
            # print(f"!!list permutations after recieving call: {list_permutations}")
        return list_permutations







test1 = [1, 2, 3, 4]
# print(permute(test1))
start_time = time()
print(f"permutations of {test1} are {permute(test1)}")
# print(f"number of permutations for {test1} is {len(permute(test1))}")
end_time = time()
print(f"time of execution: {round(end_time - start_time, 4)}")