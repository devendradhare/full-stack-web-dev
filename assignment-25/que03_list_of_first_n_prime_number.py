

# 3. Write a Python script to create a list of first N prime numbers.


li = []

for i in range(1, int(input("print prime number upto: "))):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        li.append(i)

print(li)

# [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]