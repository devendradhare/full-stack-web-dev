

# 1. Write a recursive function to print first N even natural numbers
def first_N_even_natural(N):
    if N == 0:
        return
    first_N_even_natural(N-1)
    print(N*2)

first_N_even_natural(10)

# 2. Write a recursive function to print first N even natural numbers in reverse order


def first_N_even_natural_reversed(N):
    print(N*2)
    if N == 1:
        return
    first_N_even_natural_reversed(N-1)

first_N_even_natural_reversed(10)

# 3. Write a recursive function to print squares of first N natural numbers


def square_first_N_natural_number(N):
    if N == 0:
        return
    square_first_N_natural_number(N-1)
    print(N**2)

square_first_N_natural_number(10)

# 4. Write a recursive function to print cubes of first N natural numbers.


def cubes_first_N_natural_number(N):
    if N == 0:
        return
    cubes_first_N_natural_number(N-1)
    print(N**3)

cubes_first_N_natural_number(10)

# 5. Write a recursive function to print reverse of a given number.


def reverse_number(N):
    print(N % 10, end="")
    if N//10 == 0:
        return
    reverse_number(N//10)


reverse_number(123)
