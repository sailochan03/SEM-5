def count_digits(num):
    digits = []
    while num > 0:
        digits.append(num%10)
        num //= 10

    return len(digits)

num = int(input("Enter an integer: "))
print(f"Total number of digits in {num}: {count_digits(num)}")
