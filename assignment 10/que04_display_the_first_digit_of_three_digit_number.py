# 4. Write a python script which takes a three digit number from the user and displays only its first digit.


x = int(input("Enter a three digit number: "))
x = x//100
print("the first digit =",x )