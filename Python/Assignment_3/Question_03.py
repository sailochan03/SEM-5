def find_square_sum():
    sum = 0
    for i in range(1, 51):
        if i%2 == 0:
            sum += i**2
    print(sum)

find_square_sum()
