

# 5. Write a python script to create a set of tuples, where each tuple has elements
# representing dice upper face number. Take a number N from the user and generate
# all possible tuples, in such a way that tuple elements sums to N.


N = int(input("Enter a number: "))
set_of_tpl = set()

for i in range(1,7):
    for j in range(i, 7):
        if i + j == N:
            set_of_tpl.add(tuple([i, j]))

print(set_of_tpl)
