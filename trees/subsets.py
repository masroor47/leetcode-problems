
# Input: array of unique elements
# Output: all possible subsets (the power set) in any order



def subsets(nums):

    # def recur(nums, current, end):
    #     print(f"current list: {current}")
    #     result = [current]

    #     if len(nums) - 1 <= end:
    #         return [current]

    #     for i in range(end, len(nums)):
    #         print(f"current: {current}, i: {i}")
    #         result += recur(nums, current.append(nums[i]), i)

    #     return result

    # result = recur(nums, [], 0)
    # return result

    result = []
    result.append([])

    def recur(current, rest):
        print(f"current: {current}, rest: {rest}, len: {len(rest)}")

        if len(rest) == 0:
            return


        for i in range(len(rest)):
            print(f"adding {current} and {rest[i]}")
            current.append(rest[i])
            result.append(current.copy())
            print(f"result: {result}")
            
            recur(current, rest[i+1:])
            current.pop()

    recur([], nums)
    return result

print(subsets([1, 2, 3]))