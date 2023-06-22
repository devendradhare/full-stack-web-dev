

# 5. Write a python script to count strings which ends at character 's' in a list of strings.


s = input("Enter a string: ").split(" ")

count = 0
for i in s:
    if i.endswith('s'):
        count += 1

print(count)