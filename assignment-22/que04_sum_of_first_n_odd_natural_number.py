

# 4. Write a Python script to calculate sum of first N odd natural numbers.
# 5. Write a Python script to calculate sum of first n even natural numbers.

n = int(input("Enter a number: "))
sum = 0
for i in range(1, n*2+1,2):
    sum += i

print(sum)
