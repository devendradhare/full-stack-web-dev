

# 1. Write a python script to print first N even natural numbers



x = int(input("Entet a number: "))
y = 1

while x > 0:
    print(y+y, end=" ")
    x -= 1
    y += 1