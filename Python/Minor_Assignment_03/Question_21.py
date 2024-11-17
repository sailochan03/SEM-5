def factorial(n):
    prod = 1
    while n > 0:
        prod = prod * n
        n -= 1
    return prod

n = int(input("Enter a number: "))
print(f"Factorial: {factorial(n)}")