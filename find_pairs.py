def find_pairs(numbers, target):

    pairs = []

    # Nested loops (O(n²))
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):

            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))

    return pairs


# Test example
numbers = [1, 2, 3, 4, 5]
target = 6

result = find_pairs(numbers, target)

print("Pairs:", result)

# Time Complexity Analysis
# The above solution uses nested loops, so the time complexity is O(n²).

# Optimized Approach (O(n)):
# Use a set to store numbers seen so far.

def find_pairs_optimized(numbers, target):

    seen = set()
    pairs = []

    for num in numbers:

        complement = target - num

        if complement in seen:
            pairs.append((complement, num))

        seen.add(num)

    return pairs


print("Optimized:", find_pairs_optimized(numbers, target))