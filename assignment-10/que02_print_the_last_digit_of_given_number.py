# 2. Write a python script to get the last digit from a given number (for example, if user enters 2089 then your output should be 9)


x = int(input("Enter a number: "))
x = x%10
print("the last digit of the number =", x)