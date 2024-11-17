def nth_fibonacci(num):
    if num < 1:
        return 0
    elif num == 1:
        return 1
    
    a, b = 0, 1
    for i in range(2, num):
        a, b = b, a + b
    return b

num = int(input("Enter an integer: "))
print(f"The {num}th fibonacci number is: {nth_fibonacci(num)}")
