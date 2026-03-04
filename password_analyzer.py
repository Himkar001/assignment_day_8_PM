import string
import random

special_chars = "!@#$%^&*"


def analyze_password(password):

    score = 0
    missing = []

    length = len(password)

    # Length check
    if length >= 16:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        missing.append("too short")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    repeat_ok = True
    repeat_count = 1

    for i, char in enumerate(password):

        if char.isupper():
            has_upper = True

        if char.islower():
            has_lower = True

        if char.isdigit():
            has_digit = True

        if char in special_chars:
            has_special = True

        if i > 0:
            if char == password[i-1]:
                repeat_count += 1
                if repeat_count > 2:
                    repeat_ok = False
            else:
                repeat_count = 1

    if has_upper:
        score += 1
    else:
        missing.append("uppercase")

    if has_lower:
        score += 1
    else:
        missing.append("lowercase")

    if has_digit:
        score += 1
    else:
        missing.append("digit")

    if has_special:
        score += 1
    else:
        missing.append("special character")

    if repeat_ok:
        score += 1
    else:
        missing.append("too many repeated characters")

    return score, missing


def rating(score):

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    elif score <= 6:
        return "Strong"
    else:
        return "Very Strong"


def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


while True:

    password = input("Enter password: ")

    score, missing = analyze_password(password)

    print(f"Strength: {score}/7 ({rating(score)})")

    if missing:
        print("Missing:", ", ".join(missing))

    if score >= 5:
        print("Password accepted!")
        break

    print("Try again...\n")


length = int(input("Enter length for generated password: "))

generated = generate_password(length)

print("Generated Password:", generated)

score, _ = analyze_password(generated)

print("Generated Password Strength:", rating(score))