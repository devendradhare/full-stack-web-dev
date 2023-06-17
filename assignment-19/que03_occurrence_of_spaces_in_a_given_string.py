

# 3. Write a Python script to count occurrence of spaces in a given string.
    

s = input("Enter a string: ")
count = 0

for i in s:
    if i == " ":
        count += 1

print(count)