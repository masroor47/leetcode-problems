

def lengthOfLongestSubstring(s: str) -> int:
    max_len = 0
    shift_index = 0
    dic = {}

    for i in range(len(s)):
        # char already exists
        if dic.get(s[i]) is not None:

            shift_index = dic.get(s[i])
            delta = i - shift_index
            if delta > max_len:
                max_len = delta

            # Now gotta delete instances of previous characters
            # up to this point.
            for j in range(shift_index, -1, -1):
                print(j)
                print(s[j])
                dic.pop(s[j])

            dic[s[i]] = i

        # char not in dictionary
        else:
            dic[s[i]] = i


    if len(s)-shift_index > max_len:
        max_len = len(s) - shift_index
    print(dic)
    return max_len



print(f"max substring: {lengthOfLongestSubstring('zxabcdeapqc')}")


