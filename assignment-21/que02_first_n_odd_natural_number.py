

# 2. Write a python script to print first N odd natural numbers


n = int(input("Enter a number: "))

for i in range(1, n*2+1, 2):
    print(i, end=" ")