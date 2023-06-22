
# 5. Write a python script to find maximum length word in a given text.


s = input("Enter a string : ").split(" ")
m = ""
for i in s:
    if i.__len__() >= m.__len__():
        m = i

print("max length word =",m)
