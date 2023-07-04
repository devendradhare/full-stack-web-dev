

# 4. Write a Python function to find largest sorted subsequence in a given list. 
# Return the largest subsequence as a list.(TSRS)

def largest_sorted_subsequences(li):
    list_a = []
    list_b = []
    i = 0
    for i in li:
        if list_a == [] or i >= list_a[-1]:
            list_a.append(i)
        elif len(list_b)  < len(list_a):
            list_b = list(list_a)
            list_a = [i]
        else:
            list_a = [i]
    if len(list_b)  < len(list_a):
        return list_a
    return list_b

print(largest_sorted_subsequences([3,2,1,1,2]))


