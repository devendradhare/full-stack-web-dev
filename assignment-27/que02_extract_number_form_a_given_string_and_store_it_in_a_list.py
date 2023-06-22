

# 2. Write a python script to extract numbers from a given text 
#    and store all the numbers in a list.
  

s = input("Enter a string : ")
s2 = []
for i in s:
    if i in "1234567890":
        s2.append(i)
    
print(s2)