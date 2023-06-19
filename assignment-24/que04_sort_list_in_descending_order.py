

# 4. Write a Python script to sort list elements in descending order.


li = [10, 60, 30, 40, 100, 50, 90, 70, 80, 20]

li.sort(reverse=True)
print(li)

# i = 0
# j = 0

# while i < len(li)-1:
#     while j < len(li)-i-1:
#         if li[j] < li[j+1]:
#             li[j], li[j+1] = li[j+1], li[j]
#         j += 1
#     i += 1
#     j = 0

# print(li)