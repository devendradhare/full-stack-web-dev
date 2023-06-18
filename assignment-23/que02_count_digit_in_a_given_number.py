

# 2. Write a Python script to count digits in a given number.


n = int(input("Enter a number: "))
count = 0

for i in str(n):
    count += 1

print(count)