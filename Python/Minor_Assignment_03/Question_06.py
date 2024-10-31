def palindrome_checker(s):
    reverse = ""
    for char in s:
        reverse = char + reverse
    
    if s == reverse:
        return True
    return False

s = input("Enter a string: ")
print(f"Is '{s}' a palindrome? : {palindrome_checker(s)}")