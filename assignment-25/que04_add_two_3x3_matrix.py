

# 4. Write a Python script to add two matrices each of order 3 x 3. Store matrix elements in a list of lists.

# 5. Write a Python script to create two lists from a given list of numbers in such a way
#    that the first list can have only positive numbers and second list can have only non
#    positive numbers.


l1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

l2 = [[9, 8, 7],
      [6, 5, 4],
      [3, 2, 1]]


l3 = [([(l1[i][j]+l2[i][j]) for j in range(3)]) for i in range(3)]

print(l3)
