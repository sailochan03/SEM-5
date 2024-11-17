def remove_vowels(str_):
    for i in str_:
        if i in "aeiouAEIOU":
            str_ = str_.replace(i, "")
    
    return str_


str_ = input("Enter a string: ")
print(f"New String: {remove_vowels(str_)}")