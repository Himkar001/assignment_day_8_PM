# Day 8 Take-Home Assignment – Python Loops & Algorithm Practice

**Date:** 03/03/2026
**Topics Covered:**

* for loops
* while loops
* break and continue
* loop-else
* nested loops
* time complexity (O(n) vs O(n²))

---

# Repository Structure

This repository contains solutions for all parts of the Day-8 assignment.

```
assignment_day_8_PM
│
├── password_analyzer.py
├── find_pairs.py
├── prime_debug.py
├── diamond_pattern.py
├── transaction_analyzer.py
└── README.md
```

---

# PART A — Password Strength Analyzer & Generator

## Objective

Build a Python program that analyzes the strength of a password and generates a secure password.

## Features Implemented

### Password Strength Analyzer

The program evaluates password strength based on:

**Length**

* ≥ 8 characters → +1 point
* ≥ 12 characters → +2 points
* ≥ 16 characters → +3 points

**Character Types**

* Uppercase letter → +1
* Lowercase letter → +1
* Digit → +1
* Special character (!@#$%^&*) → +1

**Additional Rule**

* No repeated characters more than 2 times in a row → +1

### Strength Rating

| Score | Rating      |
| ----- | ----------- |
| 0–2   | Weak        |
| 3–4   | Medium      |
| 5–6   | Strong      |
| 7+    | Very Strong |

### Loop Usage

* **for loop** → iterate through characters
* **while loop** → repeatedly ask for input until password strength ≥ 5

### Password Generator

The program can also generate a random password using:

```
string.ascii_letters + string.digits + string.punctuation
```

The generated password is also analyzed for strength.

---

# PART B — Interview Ready

## Q1: break vs continue

### break

Stops the loop completely.

Example:

```
for i in range(5):
    if i == 3:
        break
    print(i)
```

Output:

```
0
1
2
```

### continue

Skips the current iteration but continues the loop.

Example:

```
for i in range(5):
    if i == 3:
        continue
    print(i)
```

Output:

```
0
1
2
4
```

---

## Loop else Clause

The `else` block executes when a loop completes normally **without hitting break**.

Example:

```
numbers = [2,4,6,8]

for n in numbers:
    if n == 5:
        print("Found")
        break
else:
    print("Not found")
```

Output:

```
Not found
```

### Practical Use Case

Searching algorithms often use `loop-else` to determine whether an element was found.

---

## Q2 — Find Pairs with Target Sum

### O(n²) Solution

Uses nested loops to check all combinations.

```
def find_pairs(numbers, target):

    pairs = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):

            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))

    return pairs
```

### Time Complexity

```
O(n²)
```

---

### Optimized Solution

Uses a **set** to store previously seen numbers.

```
def find_pairs_optimized(numbers, target):

    seen = set()
    pairs = []

    for num in numbers:

        complement = target - num

        if complement in seen:
            pairs.append((complement, num))

        seen.add(num)

    return pairs
```

### Time Complexity

```
O(n)
```

---

## Q3 — Debugging Prime Function

### Original Code

```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

### Problems

1. **Inefficient loop**

   * Iterates up to `n`
   * Time complexity: `O(n)`

2. **Unnecessary checks**

   * Factors only need to be checked up to `√n`

---

### Optimized Version

```
import math

def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):

        if n % i == 0:
            return False

    return True
```

### Optimized Time Complexity

```
O(√n)
```

---

# PART C — AI Augmented Task

## Prompt Used

```
Write a Python program that prints a diamond pattern of asterisks.
The user inputs the number of rows for the upper half.
Include proper spacing and use nested loops only (no string multiplication tricks).
```

---

## AI Generated Logic

The AI solution used:

* nested loops
* spacing control
* star printing logic

Example Output (n = 4)

```
   *
  ***
 *****
*******
 *****
  ***
   *
```

---

## Evaluation

| Criteria            | Result         |
| ------------------- | -------------- |
| Spacing correctness | Correct        |
| Readability         | Good           |
| Nested loops        | Used correctly |
| Edge cases          | n = 0 handled  |
| Time complexity     | O(n²)          |

---

# PART D — Bonus Challenge

## Paytm Transaction Analyzer

### Objective

Simulate a simple analytics dashboard for transactions.

### Features Implemented

Using a **while loop**, the program collects transactions until the user enters:

```
done
```

Each transaction contains:

* amount
* transaction type (credit/debit)

---

### High Value Detection

Transactions greater than **₹10,000** are flagged as:

```
High value transaction
```

---

### Data Tracked

The program calculates:

* Total credits
* Total debits
* Net balance
* Transaction count
* Highest transaction
* Average transaction amount

---

### Bar Chart Visualization

The last **10 transactions** are displayed as a bar chart.

Example:

```
****
**
*******
```

Each `*` represents **₹1000**.

---

# Concepts Demonstrated

This assignment demonstrates understanding of:

* for loops
* while loops
* nested loops
* break and continue
* loop-else clause
* algorithm optimization
* time complexity analysis
* Python data structures

---

# Author

**Himkar Vashistha**

Day-8 Python Assignment Submission
