def unique_perms(str_):
    if len(str_) <= 1:
        return {str_}
    
    permutations = set()

    for i in range(len(str_)):
        curr_char = str_[i]
        remaining_char = str_[ : i] + str_[i+1 : ]

        for perm in unique_perms(remaining_char):
            permutations.add(curr_char + perm) 

    return permutations

str_ = "xyz"
result = unique_perms(str_)
print(f"All unique permutation of the string '{str_}' are: ")
for perm in result:
    print(perm)


