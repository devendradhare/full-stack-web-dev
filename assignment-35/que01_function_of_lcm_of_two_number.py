

# 1. Write a Python function to calculate LCM of two numben (TSRS)

def LCM(x, y):
    i = max(x, y)
    while True:
        if i % x == 0 and i % y == 0:
            return i
        i += 1

    

print(LCM(12, 18))
