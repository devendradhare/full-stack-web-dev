from functools import reduce

# Write a python script to find number of vowels in each of the string in a given list of
# strings. Use map function.


def count_vowels(s):
    count = 0
    for i in s:
        if i in "aeiouAEIOU":
            count += 1
    return count


str_list = ["devendra", "dhare", "asd", "aeiou",
            "qwerty", "qwertyuiopasdfghjklzxcvbnm"]
num_of_vowels = list(map(count_vowels, str_list))
# print(num_of_vowels)

# Write a python script to find number of digits in each of the element in a given tuple
# of numbers. Use map function.
t = (123, 24, 5673, 94387, 1, 3845)
num_of_digits = list(map(lambda x: len(str(x)), t))
# print(num_of_digits)


# Write a python script to create a list of numbers greater than a given number N
# (taken from user) for each element in a given set of numbers. Use filter function.
# given_set = set([1, 23, 345, 4567, 5678, 3, 2, 0, -34, -12])
# given_number = int(input("Enter a number : "))
# list_of_numbers = list(filter(lambda x: x > given_number, given_set))
# print(list_of_numbers)


# Write a python script to filter only int type values in a given list of elements. Use
# filter function.
l1 = [123, "123", 3.4, 342, 3+4j, "this is string", -12, -2.0, 0.0, 5]
list_of_ints = list(filter(lambda x: type(x) == int, l1))
# print(list_of_ints)

# Write a python function to calculate HCF (Highest Common Factor) of a list of
# numbers. Use reduce function.


def HCF(a, b):
    while b != 0:
        a, b = b, a % b
    return a


l2 = [12, 24, 36, 48, 60, 66]
HCF_of_list = reduce(HCF, l2)
print(HCF_of_list)
