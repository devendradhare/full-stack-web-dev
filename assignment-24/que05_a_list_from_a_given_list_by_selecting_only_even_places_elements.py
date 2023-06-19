

# 5. Write a Python script to create a list from a given list by selecting only even places
#    elements.


li = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
new_li = []
print("li     =", li)

j = 0
for i in li:
    if j % 2 == 0:
        new_li.append(i)
    j += 1

print("new li =", new_li)