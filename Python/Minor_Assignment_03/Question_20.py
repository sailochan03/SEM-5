def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False
    return True

def print_prime_in_range(start, end):
    for i in range(start, end + 1):
        if is_prime(i):
            print(i, end=' ')

print_prime_in_range(1, 100)