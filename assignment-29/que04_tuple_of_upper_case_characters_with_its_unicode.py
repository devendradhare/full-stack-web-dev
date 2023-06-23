

# 4. Write a python script to create a list of tuples, where each tuple is a pair of elements, first element is uppercase character and second element is its unicode.

list_of_tuples = []

for i in range(ord('A'), ord('Z')+1):
    list_of_tuples.append((chr(i), i))

print(list_of_tuples)
print(type(list_of_tuples[0]))