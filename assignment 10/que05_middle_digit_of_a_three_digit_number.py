# 5. Write a python script which takes a three digit number from the user and displays only its middle digit.

x = int(input("Enter a three digit number: "))
x = x//10
x = x%10
print("the middle digit =", x)