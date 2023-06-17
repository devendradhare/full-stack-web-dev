

# 5. Write a Python script to count number of digits in a given number

x = int(input("Enter a number: "))
count = 0
for i in str(x):
    count += 1

print("digits count =", count)