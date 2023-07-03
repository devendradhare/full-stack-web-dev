

# 4. Write a Python function to filter out words from a text starting from same alphabet and store them in a list.
#    Now create a dict with alphabets as key-values and list of words starting from that alphabet as data values.
#    Take text as an argument and return dict object (TSRS)

def str_dic(text):
    text = text.strip().split()
    dct = dict()
    available = ""
    for i in text:
        if i[0] in available:
            dct[i[0]].append(i)
        else:
            dct[i[0]] = [i]
            available = available + i[0]
    return dct

print(str_dic("# 4. Write a Python function to filter out words from a text starting from same alphabet and store them in a list. Now create a dict with alphabets as key-values and list of words starting from that alphabet as data values. Take text as an argument and return dict object (TSRS)"))


