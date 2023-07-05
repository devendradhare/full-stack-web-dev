

# 1. Write a recursive function to calculate sum of digits of a given number.
def sum_of_digits(N):
    if N <= 0:
        return 0
    return N % 10 + sum_of_digits(N//10)


# print(sum_of_digits(123))

# 2. Write a recursive function to calculate factorial of a given number.
def factorial(N):
    if N <= 1:
        return 1
    return N * factorial(N-1)

# print(factorial(5))


# 3. Write a recursive function to print binary of a given decimal number.
def decimal_to_binary(N):
    if N <= 1:
        return str(N % 2)
    return str(decimal_to_binary(N//2) + str(N % 2))


# N = int(input("Enter a number : "))
# print(bin(N))
# print(decimal_to_binary(N))


# 4. Write a recursive function to print octal of a given decimal number.
def decimal_to_octal(N):
    if N <= 1:
        return str(N % 8)
    return str(decimal_to_octal(N//8) + str(N % 8))


# N = int(input("Enter a number : "))
# print(oct(N))
# print(decimal_to_octal(N))


# 5. Write a recursive function to calculate sum of first N Prime numbers.
def is_prime(num, d=2):
    if d >= num:
        return True
    if num % d == 0:
        return False
    return is_prime(num, d+1)


# print(is_prime(int(input("Enter a number : "))))


def sum_of_first_N_Prime(N, prime_count=1):
    if N == 0:
        return 0
    if is_prime(prime_count):
        print(prime_count, end="+")
        return prime_count + sum_of_first_N_Prime(N-1, prime_count+1)
    return sum_of_first_N_Prime(N, prime_count+1)


print("=",sum_of_first_N_Prime(6))
