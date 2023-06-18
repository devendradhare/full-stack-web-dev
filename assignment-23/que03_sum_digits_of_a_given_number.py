

# 3. Write a Python script to calculate sum of digits of a given number.


n = int(input("Enter a number: "))
sum = 0

for i in str(n):
    sum += int(i)

print(sum)