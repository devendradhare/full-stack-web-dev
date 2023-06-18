

# 3. Write a Python script to calculate sum of cubes of first N natural numbers
# 4. Write a Python script to calculate sum of first N odd natural numbers.
# 5. Write a Python script to calculate sum of first n even natural numbers.

n = int(input("Enter a number: "))
sum = 0
for i in range(n+1):
    sum += i**3

print(sum)
