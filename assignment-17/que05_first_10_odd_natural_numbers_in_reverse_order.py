

# 5. Write a python script to print first N odd natural numbers in reverse order

x = int(input("Enter a number: "))

while x > 0:
    print(x+x-1, end=" ")
    x -= 1