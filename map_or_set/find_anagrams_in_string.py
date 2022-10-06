


def findAnagrams(s, p):
    dict = {}
    result = []

    for c in p:
        if c not in dict:
            dict[c] = 0
        dict[c] += 1

    print(dict)

    for i, c in enumerate(s):
        if c not in dict:
            dict[c] = 0
        dict[c] -= 1

        
        if i >= len(p):
            trailing = s[i-len(p)]
            if trailing not in dict:
                dict[trailing] = 0
            dict[trailing] += 1

        if dict[c] == 0:
            dict.pop(c)
        if i >= len(p) and trailing in dict and dict[trailing] == 0:
            dict.pop(trailing)

        if len(dict) == 0:
            result.append(i-len(p)+1)

    return result






test1 = "cbaebabacd"
test1p = "abc"
test2 = "abab"
test2p = "ab"


print(f"test1: {findAnagrams(test1, test1p)}")
print(f"test2: {findAnagrams(test2, test2p)}")
