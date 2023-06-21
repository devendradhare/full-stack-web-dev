

# 4. Write a python script to count words in a given string

s = input("Enter a string : ").split(" ")

words = []
for i in s:
    if i != "":
        words.append(i)

print("world count =", len(words))
