

# 1. Write a python script to check if a given string has only alphabets in it.

s = input("Enter a string : ")

for i in s:
    if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
        continue
    else:
        print("not alphabets only")
        break
else:
    print("alphabets only")

