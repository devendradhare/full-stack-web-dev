# 1. Write a Python function to calculate sum of two numbers. (TSRS)
def sum(a, b):
    return a + b

# 2. Write a Python function to calculate area of a circle(TSRS)


def circle_area(radius):
    return 3.14159 * radius**2

# 3. Write a Python function to calculate average of three numbers. (TSRS)


def average(a, b, c):
    return (a + b + c) / 3

# 4. Write a Python function to calculate compound interest. (TSRS)


def compound_interest(principal, rate, time):
    return principal * (1 + rate)**time - principal

# 5. Write a Python function to calculate volume of a cuboid. (TSRS)


def cuboid_volume(length, width, height):
    return length * width * height


result = sum(5, 3)
print("Sum:", result)  # Output: Sum: 8

result = circle_area(2)
print("Circle Area:", result)  # Output: Circle Area: 12.56636

result = average(4, 7, 9)
print("Average:", result)  # Output: Average: 6.666666666666667

result = compound_interest(1000, 0.05, 2)
print("Compound Interest:", result)  # Output: Compound Interest: 102.5

result = cuboid_volume(3, 4, 5)
print("Cuboid Volume:", result)  # Output: Cuboid Volume: 60
