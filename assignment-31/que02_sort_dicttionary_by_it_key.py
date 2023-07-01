

# 2. Sort a dictionary by its keys in descending order

d1 = {103: "payal", 101: "asdf", 100: "ABC", 102: "codendram"}
print(d1)

d2 = sorted(d1.keys())
for i in d2:
    print(i, ":", d1[i])
