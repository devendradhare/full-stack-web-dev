

# 5. Write a Python script to create two lists from a given list of numbers in such a way
#    that the first list can have only positive numbers and second list can have only non
#    positive numbers.


li = [int(e) for e in input(
    "Enter elements of the list seperated by comma : ").split(',')]

print("li = ", li)
l1 = []
l2 = []

for i in li:
    if i > 0:
        l1.append(i)
    else:
        l2.append(i)

print("l1 = ", l1)
print("l2 = ", l2)