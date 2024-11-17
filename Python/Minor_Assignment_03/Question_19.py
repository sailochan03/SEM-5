def find_gcd(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    while b != 0:
        a = b
        b = a % b
    return a

num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: "))
print(f"GCD of {num1} and {num2} is {find_gcd(num1, num2)}.")