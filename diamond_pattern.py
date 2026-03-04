# PART C — AI Augmented Task

# Prompt Used:
# "Write a Python program that prints a diamond pattern of asterisks.
# The user inputs the number of rows for the upper half.
# Include proper spacing and use nested loops only (no string multiplication tricks)."


# Improved Version with Edge Case Handling

n = int(input("Enter number of rows for upper half: "))

if n <= 0:
    print("Invalid input. Number must be greater than 0.")

else:

    # Upper half
    for i in range(1, n + 1):

        # spaces
        for j in range(n - i):
            print(" ", end="")

        # stars
        for j in range(2 * i - 1):
            print("*", end="")

        print()

    # Lower half
    for i in range(n - 1, 0, -1):

        # spaces
        for j in range(n - i):
            print(" ", end="")

        # stars
        for j in range(2 * i - 1):
            print("*", end="")

        print()


# Evaluation Notes
# Spacing correctness: Proper spacing used
# Readability: Clear nested loops
# Edge cases handled: n <= 0
# Time Complexity: O(n^2)