

# 4. Write a python script to print first N odd natural numbers

x = int(input("Enter a number: "))
y = 1

while x > 0:
    print(y, end=" ")
    x -= 1
    y += 2