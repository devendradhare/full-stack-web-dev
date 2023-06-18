

# 4. Write a Python script to print binary equivalent of a given decimal number. (Do not use bi() method)


n = int(input("Enter a number: "))
bi = ""

print("using bin func =",bin(n))

while n > 0:
    bi = str(n%2) + bi
    n = n // 2

print("using loop =      ",bi)