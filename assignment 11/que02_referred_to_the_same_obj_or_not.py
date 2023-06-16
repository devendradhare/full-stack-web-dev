# 2. Write a python script to input two strings from the user
#    and display whether the two variables referred to the same object or not. Print True or False.


a = input("Enter a string:       ")
b = input("Enter another string: ")
print(id(a), id(b), sep="\n")

print(a is b)



# if(id(a) == id(b)):
#    print(True)
# else:
#    print(False)
