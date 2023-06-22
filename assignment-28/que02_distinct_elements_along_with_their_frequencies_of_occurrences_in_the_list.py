

# 2. Write a python script to print distinct elements along with their frequencies of occurrences in the list.


s = input("Enter a string: ")

s2 = []
for i in s:
    if i not in s2:
        print(i, "=", s.count(i))
        s2.append(i)