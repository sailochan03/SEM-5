def calculator():
    print("Choose operation:\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Exit\n")

    while True:
        ch = input("Enter Operation: ")

        if ch == '5':
            print("Exiting Calculator ...")
            print("BYEEEE")
            break

        if ch in ['1', '2', '3', '4']:
            a = float(input("Enter num 1: "))
            b = float(input("Enter num 2: "))

            if ch == '1':
                print(f"{a} + {b} = {a + b}")
            elif ch == '2':
                print(f"{a} - {b} = {a - b}")
            elif ch == '3':
                print(f"{a} * {b} = {a * b}")
            elif ch == '4': 
                if b == 0:
                    print("Division with 0 is not allowed")
                    continue
                print(f"{a} / {b} = {(a / b):.2f}")
            else:
                print("Enter valid input")

calculator()



