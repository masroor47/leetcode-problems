
def lengthOfLongestSubstring(s: str) -> int:

    print("received", s)

    max_len = 0
    curr_len = 0
    shift_index = -1
    new_shift_index = 0
    dic = {}
    #     ^ *   ^     *
    # A B C D E C Z X D R T  Y
    # 0 1 2 3 4 5 6 7 8 9 10 11

    # b
    # 0

    # a a b
    # 0 1 2

    for i in range(len(s)):
        print("i:", i, "char:", s[i])
        if dic.get(s[i]) is not None:
            new_shift_index = dic.get(s[i])

            curr_len = i - new_shift_index

            # delta = i - new_shift_index
            # if delta > max_len:
            #     max_len = delta

            print(f"i {i}, new shift {new_shift_index}, delta: {curr_len}")
            for j in range(new_shift_index, shift_index, -1):
                dic.pop(s[j])

            shift_index = new_shift_index
            dic[s[i]] = i

        else:
            dic[s[i]] = i
            curr_len += 1
            if curr_len > max_len:
                max_len = curr_len

    new_delta = len(s) - 1 - shift_index
    if new_delta > max_len:
        max_len = new_delta

    return max_len



test1 = 'abcabcbb'
print(f"max substring of {test1} is {lengthOfLongestSubstring(test1)}\n")

test2 = 'bbbbb'
print(f"max substring of {test2} is {lengthOfLongestSubstring(test2)}\n")

test3 = 'pwwkew'
print(f"max substring of {test3} is {lengthOfLongestSubstring(test3)}\n")

test4 = 'b'
print(f"max substring of {test4} is {lengthOfLongestSubstring(test4)}\n")