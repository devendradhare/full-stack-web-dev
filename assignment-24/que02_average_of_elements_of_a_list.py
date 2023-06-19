

# 2. Write a Python script to calculate average of elements of a list.
# 3. Write a Python script to create a list of squares of numbers of a given list.
# 4. Write a Python script to sort list elements in descending order.
# 5. Write a Python script to create a list from a given list by selecting only even places
#    elements.


# li = [10,20,30,40,50,60,70,80,90,100]
li = [10,20,30]

# avg = 0
# for i in li:
#     avg += i

# avg = avg/li.__len__()

avg = sum(li)/li.__len__()
    
print("average =", avg)