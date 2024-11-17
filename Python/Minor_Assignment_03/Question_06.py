def is_palindrome(s):
    reverse = ""
    for char in s:
        reverse = char + reverse
    
    if s == reverse:
        return True
    return False

s = input("Enter a string: ")
print(f"Is '{s}' a palindrome? : {is_palindrome(s)}")