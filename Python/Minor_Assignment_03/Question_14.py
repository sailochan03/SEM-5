def is_armstrong(num):
    str_num = str(num)
    power = len(str_num)
    
    armstrong = 0
    for i in str_num:
        armstrong += int(i) ** power

    return armstrong == num
    
num = int(input("Enter num: "))
print(f"Is '{num}' an armstrong number: {is_armstrong(num)}")