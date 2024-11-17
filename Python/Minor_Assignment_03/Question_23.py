def vowel_index(str_):
    indices = []

    for index, char in enumerate(str_):
        if char in "aeiouAEIOU":
            indices.append(index)

    return indices

input_str = input("Enter a string: ")
print(f"Indices of vowels in '{input_str}' : {vowel_index(input_str)}.")