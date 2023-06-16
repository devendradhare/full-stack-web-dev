# 5. Write a python script to print greater among three numbers. Print number only once
#    even if the numbers are the same.

a = int(input("Enter first number  : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number  : "))

if a > b:
    print(a if a > c else c)
else:
    print(b if b > c else c)


print(a if a > c else c if a > b else b if b > c else c)
