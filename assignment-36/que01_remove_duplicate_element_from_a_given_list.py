

# 1. Write a Python function to remove duplicate elements from a given list. (TSRS)

def remove_duplicates(l):
    new_list = []
    for i in l:
        if i not in new_list:
            new_list.append(i)
    return new_list


print(remove_duplicates(
    ['a', 'b', 'c', 'a', 'b', 'c', 1, 2, 3, 1, 2, 3, 5, 4, 5, 4]))


