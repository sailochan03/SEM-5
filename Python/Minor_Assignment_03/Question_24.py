from string import punctuation as p

def remove_punctuations(str_):
    return ''.join(ch for ch in str_ if ch not in p)

str_ = input("Enter a string: ")
print(f"After removing punctuations: {remove_punctuations(str_)}")