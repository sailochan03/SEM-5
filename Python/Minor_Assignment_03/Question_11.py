def can_form_palindrome(str_):
    char_list = [ch.lower() for ch in str_ if ch.isalnum()]
    char_count = {}

    for ch in char_list:
        char_count[ch] = char_count.get(ch, 0) + 1
   
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
    
    return odd_count <= 1
            
str_ = input("Enter a string: ")
print(f"Can '{str_}' form a palindrome: {can_form_palindrome(str_)}")