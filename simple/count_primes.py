import math

# Input: int N
# Output: number of primes that are less than N
# n = 2, return 0
# n = 3, 2 is prime, so return 1


def count_primes(n: int) -> int:

    count = 0
    if n <= 1:
        return 0
    for i in range(2, n):
        sqrt = math.floor(math.sqrt(i))
        print(f"i: {i},    sqrt: {sqrt}")
        isprime = True
        
        for j in range(2, sqrt+1):
            print(f"j: {j}")
            if i % j == 0:
                print(f"{i} is not prime")
                isprime = False
                break
        
        if isprime:
            print(f"{i} is prime (?)")
            count += 1
        print()
    return count




test1 = 11
print(f"primes until {test1}: {count_primes(test1)}")