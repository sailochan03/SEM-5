def binary_to_decimal(binary):
    decimal = 0
    power = 0
    while binary > 0:
        digit = binary % 10
        if digit == 1:
            decimal += 2**power
        binary //= 10
        power += 1
    return decimal

def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal //= 2
    return binary if binary else "0"

choice = int(input("1. Binary to Decimal \n2. Decimal to binary \nChoose an operation: "))

if choice == 1:
    binary = int(input("Enter binary number: "))
    print(f"Decimal number: {binary_to_decimal(binary)}")
elif choice == 2:
    decimal = int(input("Enter decimal number: "))
    print(f"Decimal number: {decimal_to_binary(decimal)}")
else: 
    print("Invalid choice.")


