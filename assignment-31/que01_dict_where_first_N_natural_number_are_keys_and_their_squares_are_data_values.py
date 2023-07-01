

# 1. Create a dict object where first N natural numbers are keys and their squares are data values.

d1 = {x: x**2 for x in range(1, int(input("Enter a number : "))+1)}
print(d1)
