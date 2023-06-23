

# 3. Write a python script to create a list of tuples from a given list of strings, where each tuple is a collection of strings begin with the same character.


list_str = ["abcd",  "coding", "qwerty",  "devendra", "heppy",
            "holi", "india", "dhare", "qwerty2", "codendram", "asdf", ]

list_of_tuples = []

list_str = sorted(list_str)
print(list_str)

character = list_str[0][0]
temp_list = []
for i in list_str:
    if i[0] == character:
        temp_list.append(i)
    else:
        character = i[0]
        list_of_tuples.append(tuple(temp_list))
        temp_list = []
        temp_list.append(i)
list_of_tuples.append(tuple(temp_list))

print(list_of_tuples)
