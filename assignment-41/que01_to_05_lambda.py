

# 1. Write a lambda expression to check if a number is even.
# print((lambda x: x % 2 == 0)(9))

# 2. Write a lambda expression to find nth term of Fibonacci series
Fibonacci = (lambda n, a=-1, b=1: a+b if n == 1 else Fibonacci(n-1, b, a+b))
# print(Fibonacci(11))
# 0 1 1 2 3 5 8 13 21 34 55

# 3. Write a lambda expression to calculate area of a circle.
# area_of_circle = lambda x: 22/7*x**2
# print(area_of_circle(10))

# 4. Write a lambda expression to find HCF of two numbers.

# HCF = lambda a, b: a if b == 0 else HCF(b, a%b)
# print(HCF(24,36))
# 5. Write a lambda expression to count words in a given text.
words_in_text = lambda text: len(text.split())
print(words_in_text("asdf devendra asdf, asd"))

    