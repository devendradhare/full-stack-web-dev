# 1. Write a python script to remove the last digit from a given number. 
#    (for example, if user enters 2534 then your output should be 253)


x = int(input("Enter a number: "))
x = x//10
print("Number without last digit = ", x)