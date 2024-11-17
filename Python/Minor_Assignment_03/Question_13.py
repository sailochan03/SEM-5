def roman_to_int(roman):
    values = {"I" : 1,
             "V" : 5,
             "X" : 10,
             "L" : 50,
             "C" : 100,
             "D" : 500, 
             "M" : 1000}
    
    total = 0
    prev_value = 0

    for i in reversed(roman):
        current_value = values[i]

        if current_value < prev_value:
            total = total - current_value
        else:
            total = total + current_value

        prev_value = current_value
    
 
    return total

roman = input("Enter roman number: ")
print(f"The integer equivalent '{roman}' is {roman_to_int(roman)}.")


