

# 2. Create two sets from a given set of numbers to separate even and odd numbers.

 
s1 = set(range(21))
print("s1:", s1, type(s1))

s2 = set()
s3 = set()


for i in s1:
    if i % 2 == 0:
        s2.add(i)
    else:
        s3.add(i)

print("s2:", s2, type(s2))
print("s3:", s3, type(s3))
