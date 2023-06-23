

# 1. Write a python script to create a tuple from a given list.

l = input("Enter a list separated by commas: ").split(",")
print("type of l =", type(l), l)

t = tuple(l)
print("type of t =", type(t), t)
