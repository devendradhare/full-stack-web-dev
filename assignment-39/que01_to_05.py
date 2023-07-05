

# 1. Write a recursive function to calculate sum of first N natural numbers.
def sum_first_N_natural(N):
    if N == 0:
        return 0
    return N+sum_first_N_natural(N-1)


print(sum_first_N_natural(10))


# 2. Write a recursive function to calculate sum of first N odd natural numbers.
def sum_first_N_odd_natural(N):
    if N == 0:
        return 0
    return N*2-1+sum_first_N_odd_natural(N-1)


print(sum_first_N_odd_natural(3))


# 3. Write a recursive function to calculate sum of first N even natural numbers.
def sum_first_N_even_natural(N):
    if N == 0:
        return 0
    return N*2 + sum_first_N_even_natural(N-1)


print(sum_first_N_even_natural(3))


# 4. Write a recursive function to calculate sum of squares of first N natural numbers.
def sum_of_squares_N_natural(N):
    if N <= 0:
        return 0
    return N**2 + sum_of_squares_N_natural(N-1)


print(sum_of_squares_N_natural(3))


# 5. Write a recursive function to calculate sum of cubes of first N natural numbers.
def sum_of_cubes_N_natural(N):
    if N <= 0:
        return 0
    return N**3 + sum_of_cubes_N_natural(N-1)


print(sum_of_cubes_N_natural(3))
