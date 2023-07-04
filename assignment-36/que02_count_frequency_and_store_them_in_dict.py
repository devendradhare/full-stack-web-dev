

# 2. Write a Python function to count frequency of each element of the list and store list elements in
#    the dict object as keys and element frequency as data values (TSRS)

def count_frequency(li):
    dct = {}
    for i in li:
        dct[i] = li.count(i)
    return dct


print(count_frequency([1, 2, 3, 4, 5, 1, 2, 4, 2]))

