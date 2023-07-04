

# 1. Write a recursive function to print first N natural numbers
def first_N_natural_number(N):
    if N == 0:
        return
    first_N_natural_number(N-1)
    print(N)


# 2. Write a recursive function to print first N natural numbers in reverse order
def first_N_natural_number_reversed(N):
    print(N)
    if N == 1:
        return
    first_N_natural_number_reversed(N-1)


# 3. Write a recursive function to print first N odd natural numbers
def first_N_odd_natural(N):
    if N <= 0:
        return
    first_N_odd_natural(N-1)
    print(N*2-1)


# 4. Write a recursive function to print first N odd natural numbers in reverse order.
def first_N_odd_natural_reversed(N):
    print(N*2-1)
    if N <= 1:
        return
    first_N_odd_natural_reversed(N-1)


# 5. Write a recursive function to print MySirG N times on the screen.
def print_MySirG_N_times(N):
    if N == 0:
        return
    print_MySirG_N_times(N-1)
    print("MySirG")


# first_N_natural_number(10)
# first_N_natural_number_reversed(10)
# first_N_odd_natural(10)
# first_N_odd_natural_reversed(10)
# print_MySirG_N_times(5)
