

# 3. Given a set of five player names. Write a Python script to form all possible pairs
# of players that is selecting two players at a time.

 
s1 = set(["devendra", "ram", "codendra", "rahul", "akshay"])
print("s1:", s1, type(s1))

s2 = list(s1)

i = 0
while i < len(s2)-1:
    j = i+1
    while j < len(s2):
        print(s2[i], s2[j])
        j += 1
    i += 1
