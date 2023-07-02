

# 1. Write a Python function to print first N odd natural numbers. (TSRN)

def first_n_odd(n):
    for i in range(1, n*2+1, 2):
        print(i, end=" ")

# 2. Write a Python function to print first N Prime numbers (TSRN)


def first_n_prime(n):
    i = 1
    while n:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end=" ")
            n -= 1
        i += 1


# 3. Write a Python function to print all prime numbers between two given numbers (TSRN)

def prime_between(a, b):
    for i in range(a, b):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end=" ")


# 4. Write a Python function to print first N terms of Fibonacci series (TSRN)

def fibonacci(n):
    a, b = -1, 1
    while n:
        print(a+b, end=" ")
        a,b = b, a+b
        n -= 1
# 5. Write a Python function to print all factors of a given number (TSRN)

def factors(n):
    for i in range(1,n+1):
        if n%i == 0:
            print(i, end=" ")


# first_n_odd(9)
# first_n_prime(30)
# prime_between(1,100)
# fibonacci(20)
factors(100)
