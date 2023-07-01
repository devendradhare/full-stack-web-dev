

# 01. Write a Python function to check if a number is even. (TSRS)
def is_even(number):
    return number % 2 == 0

# 02. Write a Python function to find greater among three numbers(TSRS)


def find_greater(a, b, c):
    return max(a, b, c)

# 03. Write a Python function to check whether a number is Prime (TSRS)


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# 04. Write a Python function to check if an year is leap year (TSRS)


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# 05. Write a Python function to calculate factorial of a number (TSRS)


def calculate_factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers."
    elif number == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        return factorial

# Function calls for testing


number = 4
result = is_even(number)
print(number, "is even:", result)  # Output: 4 is even: True

a, b, c = 5, 9, 3
result = find_greater(a, b, c)
print("Greater number:", result)  # Output: Greater number: 9

number = 17
result = is_prime(number)
print(number, "is prime:", result)  # Output: 17 is prime: True

year = 2024
result = is_leap_year(year)
print(year, "is a leap year:", result)  # Output: 2024 is a leap year: True

number = 6
result = calculate_factorial(number)
print("Factorial of", number, "is:", result)  # Output: Factorial of 6 is: 720
