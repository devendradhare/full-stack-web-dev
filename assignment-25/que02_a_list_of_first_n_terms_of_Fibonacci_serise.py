

# 2. Write a Python script to create a list of first N terms of a Fibonacci series


# 0 1 1 2 3 5 8 13 21 34 55 89 ...

li = []
a = -1
b = 1
for i in range(0, int(input("Enter a number: "))):
    li.append(a + b)
    a, b = b, a + b

print(li)
