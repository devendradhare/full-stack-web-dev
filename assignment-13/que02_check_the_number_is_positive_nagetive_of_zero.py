# 2. Write a python script to check whether a given number is positive, negative or zero.
# 3. Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots


x = int(input("Enter a number: "))

print(f"the number {x} is", "positive" if x > 0 else "negative" if x < 0 else "zero")