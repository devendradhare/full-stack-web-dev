

# 1. Write a python script to reverse a string word wise 
#    (for example- "mysirg education services" is a given string and 
#    resulting string should be "services education Mysirg")


s = input("Enter a string : ").split(" ")
s2 = []
for i in s:
    s2.insert(0, i)
    
s2 = " ".join(s2)
print(s2)