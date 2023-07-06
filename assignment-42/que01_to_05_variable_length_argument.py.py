

# 1. Write a function which receives variable length arguments to calculate average of
# integers. It returns the average of numbers.
def average(*args):
    return sum(args)/len(args)


# print(average(1, 2, 3))

# 2. Write a function which receives variable length arguments to find greatest element.
# It returns the greatest element
def greatest_element(*args):
    return max(args)

# print(greatest_element(2,3,1))

# 3. Write a function which receives variable length arguments to filter odd and even
# numbers. Store all odd numbers in a list and all even numbers in another list. Store
# both the lists in a tuple and return.


def filter_even_odd(*args):
    even = []
    odd = []
    for i in args:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return tuple([odd, even])


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# print(filter_even_odd(*li))


# 4. Write a function which takes variable length arguments to receive strings. Return
# the list of max length string or strings if multiple strings have the same length.
def max_length_string(*args):
    maxlen = max(len(i) for i in args)
    return [i for i in args if len(i) == maxlen]

# print(max_length_string("asdf", "qwe", "qwer", "addd"))

# 5. Write a function which takes variable length arguments to receive integers. Filter out
# Prime numbers and return a list of those Prime numbers.
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


def filter_prime_numbers(*args):
    return [i for i in args if is_prime(i)]


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(filter_prime_numbers(*li))


