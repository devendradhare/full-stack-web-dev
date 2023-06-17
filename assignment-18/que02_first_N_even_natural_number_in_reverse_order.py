

# 2. Write a python script to print first N even natural numbers in reverse order
    

x = int(input("Enter a number: "))

while x > 0:
    print(x+x, end=" ")
    x -= 1