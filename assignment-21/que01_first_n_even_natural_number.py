

# 1. Write a python script to print first N even natural numbers.



n = int(input("Enter a number: "))

for i in range(2, n*2+1, 2):
    print(i, end=" ")