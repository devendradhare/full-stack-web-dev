

# 3. Write a Python function to find numbers in a given text, store numbers in a list and return list. (TSRS)

def find_numbers(text):
    num = "1234567890"
    lst = []
    currnt_number = ""
    for i in text:
        if i in num: 
            currnt_number += i
        elif currnt_number != "":
            lst.append(int(currnt_number))
            currnt_number = ""
    if currnt_number != "":
        lst.append(int(currnt_number))
    return lst


print(find_numbers("hello 123 dvn 234 sdkfjwer3 23 3e 423 234lkj;l2k4j 34lj 34"))


