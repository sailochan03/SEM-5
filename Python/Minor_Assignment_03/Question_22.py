def arithematic_progression(a, d):
    for i in range(10):
        x = a + i * d
        print(x, end=" ")

a = int(input("Enter first term: "))
d = int(input("Enter common difference: "))
arithematic_progression(a, d)