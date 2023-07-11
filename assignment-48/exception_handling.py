

# 1. Define a Python function to calculate factorial of a number. Handle all possible exceptions.
def factorial(N):
    factorial = 1
    while N:
        factorial *= N
        N -= 1
    return factorial


# try:
#     a = int(input("Enter a number: "))
#     print(factorial(a))
# except ValueError as e:
#     print("Invalid input")


# 2. Define a function to find greater value among three given data. Handle all possible exceptions.
def find_greatest_value(data1, data2, data3):
    try:
        max_value = max(data1, data2, data3)
        return max_value
    except TypeError:
        print("Error: The input values must be comparable.")
    except Exception as e:
        print("An error occurred:", str(e))


# Example usage:
data1 = 10
data2 = 15
data3 = "asf"
# print(find_greatest_value(data1, data2, data3))


# 3. How many else can be used with one try block?
# answer = only one


# 4. When finally is executed?
# answer = every time whenever try block is executed


# 5. Can we write try block without except clause?
# answer = we can use finally and else instad of except
