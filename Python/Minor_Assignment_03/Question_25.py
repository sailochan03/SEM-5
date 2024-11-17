def are_coprimes(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1 == 1

num1, num2 = int(input("Enter first number: ")), int(input("Enter second number: "))
print(f"{num1} and {num2} are coprimes : {are_coprimes(num1, num2)}")