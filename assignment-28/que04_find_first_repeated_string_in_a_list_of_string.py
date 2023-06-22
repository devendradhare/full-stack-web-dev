

# 4. Write a python script to find first repeated string in a list of strings


s = input("Enter a string: ")
s2 = input("find first repeated string: ")

s3 = s[s.find(s2)+s2.__len__()::].find(s2)+s.find(s2)+s2.__len__()
print(s3)