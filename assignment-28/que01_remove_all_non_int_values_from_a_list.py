

# 1. Write a python script to remove all non int values from a list


s = input("Enter a string: ")
s2 = ""
for i in s:
    if i in "1234567890":
        s2 += i
s = s2

print(s)