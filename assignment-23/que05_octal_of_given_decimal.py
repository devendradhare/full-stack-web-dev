

# 5. Write a Python script to print the octal equivalent of a given decimal number. (Do not use oct() method)


n = int(input("Enter a number: "))
oc = ""

print("using bin func =", oct(n))

while n > 0:
    oc = str(n % 8) + oc
    n = n // 8


print("using loop =      ", oc)
