# 1. Write a python script to check whether a given number is positive or non-positive


x = int(input("Enter a number: "))

print("positive" if x > 0 else "negative")

if x <= 0:
    print(f"{x} is non-positive")
else:
    print(f"{x} is positive")