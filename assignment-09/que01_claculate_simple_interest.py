# 1. Write a python script to calculate simple interest.


print("simple interest calculator")
p = float(input("Enter your principal amount: "))
i = float(input("Enter your interest rate: "))
t = float(input("Enter time (in years): "))
A = (p*i*t)/100
print("simple interest =", A)
