

# 5. Write a Python function to find all the common factors of two given numbers. Return a tuple of such factors (TSRS)

def common_factors(a, b):
    common_factors_list = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            common_factors_list.append(i)
    return tuple(common_factors_list)


result = common_factors(24, 36)
print(result)
