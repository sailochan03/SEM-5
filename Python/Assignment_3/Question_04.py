def string_reverse(s):
    reverse = ""
    for char in s:
        reverse = char + reverse
    return reverse


s = input("Enter a string: ")
print(f"Reverse: {string_reverse(s)}")