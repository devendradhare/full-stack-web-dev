

# 3. Write a Python function to create a list of Prime numbers between two given numbers (TSRS)

def prime_between(a, b):
    a, b = min(a, b), max(a, b)
    prime_list = []
    while a <= b:
        i = 2
        while i < a/2:
            if a % i == 0:
                break
            i += 1
        else:
            prime_list.append(a)
        a += 1
    return prime_list

print(prime_between(1, 100))

    