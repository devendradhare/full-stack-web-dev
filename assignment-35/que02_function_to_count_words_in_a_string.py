

# 2. Write a Python function to count words in a string (TSRS)

def count_words(st):
    st = st.strip().split()
    print(st)
    word_count = 0
    for i in st:
        if i != "":
            word_count += 1
    return word_count


a = count_words("asdf              asd      a\ndvn")
print(a)


