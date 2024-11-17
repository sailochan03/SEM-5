def replace_vowels(str_):
    for i in str_:
        if i in "aeiouAEIOU":
            str_ = str_.replace(i, '*')
    return str_

str_ = input("Enter a string: ")
print(f"Replaced vowels string: {replace_vowels(str_)}")