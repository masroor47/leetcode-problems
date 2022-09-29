


def backspace_compare(s, t):
    initial = [s, t]
    final = []
    for idx, str in enumerate(initial):
        final.append([])
        print(f"working with sring {str}")
        for i in range(len(str)):
            if final[idx] and str[i] == '#':
                final[idx].pop()
            elif str[i] != '#':
                final[idx].append(str[i])

        

    print(final)

    if "".join(final[0]) == "".join(final[1]):
        return True
    return False




print(backspace_compare("ab#c", "ad#c"))
print(backspace_compare("ab##", "c#d#"))
print(backspace_compare("a#c", "b"))
