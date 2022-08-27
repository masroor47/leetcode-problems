



def isPalindrome(x: int) -> bool:
    number = str(x)
    for i in range(len(number)//2):
        if number[i] != number[-(i+1)]:
            return False

    return True


print(isPalindrome(121))

print(isPalindrome(-121))

print(isPalindrome(10))
