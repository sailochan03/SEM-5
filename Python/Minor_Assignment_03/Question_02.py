def find_numbers():
    nums = []
    for i in range(100, 501):
        if i%3 == 0 and i%5 == 0:
            nums.append(i)
            
    print(nums)

find_numbers()