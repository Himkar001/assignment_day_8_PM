import math

# Original buggy function (for reference)
def is_prime_buggy(n):

    if n < 2:
        return False

    for i in range(2, n):  # inefficient loop
        if n % i == 0:
            return False

    return True


# Optimized version
def is_prime(n):

    if n < 2:
        return False

    # only check until sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):

        if n % i == 0:
            return False

    return True


# Test cases
numbers = [1, 2, 3, 4, 5, 16, 17, 29]

for num in numbers:

    if is_prime(num):
        print(num, "is Prime")
    else:
        print(num, "is Not Prime")

        # Issues in original code:
# 1. Performance issue:
#    The loop runs from 2 to n, making the time complexity O(n)

# 2. Optimization:
#    A number only needs to be checked up to sqrt(n)
#    because if n = a * b, one of the factors must be <= sqrt(n)

# Optimized Time Complexity:
# O(√n)