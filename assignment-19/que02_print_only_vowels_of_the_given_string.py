

# 2. Write a Python script to print only vowels of the given string


s = input("Enter a string: ")

for i in s:
    if(i in "aeiouAEIOU"):
        print(i)