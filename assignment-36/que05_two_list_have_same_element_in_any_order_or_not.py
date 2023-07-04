

# 5. Write a Python function to check if two given list have same elements in any order or not. 
#    Return True or False. (TSRS)


def is_element_same(l1, l2):
    if len(l1) != len(l2):
        return False
    for i in l1:
        if l1.count(i) != l2.count(i):
            return False
    return True


print(is_element_same([1,2,"a",3,4,"asdf",2,2], [1,2,4,2,3,2,"asdf", "a"]))
