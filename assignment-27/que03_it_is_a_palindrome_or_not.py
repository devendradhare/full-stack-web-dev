
# 3. Write a python script to check whether it is a palindrome or not.


s = input("Enter a string : ")

print("palindrome" if s == s[::-1] else "not palindrome")