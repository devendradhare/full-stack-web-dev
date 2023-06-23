

# 5. Write a python script to find the sum of all odd numbers stored in a tuple.

t = tuple(range(1,11))
sum = 0

for i in t:
    if i%2 == 1:
        sum += i

print("t =", t)
print("sum =", sum)