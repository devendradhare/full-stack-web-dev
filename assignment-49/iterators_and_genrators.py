

# 1. Write a generator to produce first N prime numbers
def generate_next_prime():
    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    i = 1
    while True:
        if is_prime(i):
            yield i
        i += 1


# next_prime = generate_next_prime()
# while True:
#     print(next(next_prime))
#     input()


# 2. Write a generator to produce first N terms of the Fibonacci series.
def generate_next_fibonacci():
    a, b = -1, 1
    while True:
        yield a + b
        a, b = b, a + b

# next_fib = generate_next_fibonacci()
# while True:
#     print(next(next_fib),end=" ")
#     input()


# 3. Write a generator to produce squares of first N natural numbers.
def generate_next_square():
    i = 1
    while True:
        yield i**2
        i += 1

# next_square = generate_next_square()
# while True:
#     print(next(next_square),end=" ")
#     input()


# 4. Use iter and next method to print values of a given list using while loop which works equivalent to for loop.
lst = [1, 2, 3, 4, 5, 6, 7]
it = iter(lst)
# while True:
#     try:
#         print(next(it),end=" ")
#     except:
#         break


# 5. Use iter and next method to check if all the elements of a list are even numbers using while loop which should work equivalent to for loop
lst = [2, 4, 6, 8, 10]
it = iter(lst)
while True:
    try:
        if next(it) % 2:
            print(False)
            break
    except:
        print(True)
        break
