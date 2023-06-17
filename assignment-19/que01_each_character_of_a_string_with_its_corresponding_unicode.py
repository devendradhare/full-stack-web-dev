

# 1. Write a python script to print each character of a string with its corresponding Unicode.


s = input("Enter a string: ")

for i in s:
    print(i, "=", ord(i))