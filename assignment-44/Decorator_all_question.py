

# 1.  Write a function to calculate HCF of two numbers. Define a decorator for HCF
#     function to tell whether the two numbers are co-prime or not.
def co_prime(HCF_func):
    def coprime(a, b):
        if HCF_func(a, b) == 1:
            print("co_prime")
        else:
            print("not co_prime")
        return HCF_func(a, b)
    return coprime


@co_prime
def HCF(a, b):
    while b:
        a, b = b, a % b
    return a


# print(HCF(11, 22))


# 2.  Define a decorator to display "Happy New Year" message at the beginning.
def happy_new_year(func):
    def wish_new_year():
        print("Happy New Year")
        return func()
    return wish_new_year

# 3.  Define a decorator to display "Good Bye" message at the end.


def good_bye_decorator(func):
    def good_bye(name):
        my_func = func(name)
        print("Goodbye")
        return my_func
    return good_bye


@good_bye_decorator
def hello(name):
    print(f"hello {name}!")

# hello("devendra dhare")

# 4.  Write a function to check if a given number N is a Prime or not. Define a decorator
#     to print total number of Prime numbers before N.


def prime_before_N(func):
    def prime_upto_N(N):
        while N:
            for i in range(2, N):
                if N % i == 0:
                    break
            else:
                print(N, end=" ")
            N -= 1
        return func(N)
    return prime_upto_N


@prime_before_N
def is_prime(N):
    for i in range(2, N):
        if N % i == 0:
            return False
    return True


# print(is_prime(97))


# 5.  Write a function to check if the given sides of a triangle can form a valid triangle or
#     not. Define a decorator to print "Right Angled Triangle" if the triangle is right angled
#     triangle.

def right_triangle_decorator(func):
    def wrapper(a, b, c):
        is_triangle = func(a, b, c)
        if is_triangle and is_right_triangle(a, b, c):
            print("Right Angled Triangle")
        return is_triangle

    return wrapper


@right_triangle_decorator
def is_valid_triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return True
    return False


def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2


# Test Cases
# print(is_valid_triangle(3, 4, 5))  # Right Angled Triangle
# print(is_valid_triangle(5, 12, 13))  # Right Angled Triangle
# print(is_valid_triangle(4, 5, 6))  # Not a Right Angled Triangle
# print(is_valid_triangle(7, 8, 12))  # Not a Right Angled Triangle
# print(is_valid_triangle(7, 8, 120))  # Not a Triangle
# print(is_valid_triangle(700, 8, 12))  # Not a Triangle
