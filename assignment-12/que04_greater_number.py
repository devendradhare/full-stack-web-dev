# 4. Write a python script to print greater between two numbers.
#    Print number only once even if the numbers are the same.

x, y = int(input("Enter two numbers: ")), int(input())
print(x if x > y else y)
