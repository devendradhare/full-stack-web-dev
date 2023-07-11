

# 1. Write a function to write a given string in a given file.
def write(filename, text=None):
    try:
        f = open(filename, 'w')
        f.write(text)
        f.close()
    except FileNotFoundError as e:
        print(e)

# write("file1.txt", "devendra dhare")


# 2. Write a function to read text from a given file and display it on the screen.
def read(filename):
    try:
        f = open(filename, 'r')
        text = f.read()
        print(text)
        f.close()
    except FileNotFoundError as e:
        print(e)

# read("file1.txt")


# 3. Write a function to copy one file data to another file.
def copy(file1, file2):
    try:
        f = open(file1, 'r')
        text = f.read()
        f.close()

        f2 = open(file2, 'w')
        f2.write(text)
        f2.close()
    except FileNotFoundError as e:
        print(e)

# copy("file1.txt", "file2.txt")


# 4. Write a function to read and store all the numbers found in a given text file into a list.
def filter_numbers(filename):
    try:
        f = open(filename, 'r')
        text = f.read()
        f.close()
        digits = "0123456789"
        num_list = []
        number = ""
        for i in text:
            if i in digits:
                number = number + i
            elif number != "":
                num_list.append(int(number))
                number = ""
        if number != "":
            num_list.append(int(number))
        return num_list

    except FileNotFoundError as e:
        print(e)


# print(filter_numbers("file1.txt"))


# 5. A file contains N lines, each line consist of a name and age separated by comma.
# Write a function to read this file and store data in a dict object with name as keys
# and age as value. Assuming the names are unique.
def name_age_dict(filename):
    try:
        f = open(filename, 'r')
        text = f.read()

        dct = dict()
        for i in text.split("\n"):
            i = i.split(",")
            dct[i[0]] = i[1]

        f.close()
        return dct
    except FileNotFoundError as e:
        print(e)


print(name_age_dict("file2.txt"))
