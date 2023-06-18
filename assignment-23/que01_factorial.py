

# 1. Write a Python script to calculate factorial of a given number.


n = int(input("Enter a number: "))
facto = 1

for i in range(2,n+1):
    facto *= i

print(facto)