def is_vowel(char):
    char.lower()
    if char in 'aeiouAEIOU':
        return True
    return False
    
char = input("Enter a character: ")
print(f"'{char}' is a vowel: {is_vowel(char)}")