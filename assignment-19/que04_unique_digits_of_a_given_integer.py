

# 4. Write a Python script to print unique digits of a given integer.

num = int(input("Enter a number: "))
num = str(num)
a = 0

for i in num:
    if num.index(i) == a:   
        print(i, end="")
    a += 1

# for i in str(num):
#     if str(a) in str(num):
#         print(a)
#     a += 1


