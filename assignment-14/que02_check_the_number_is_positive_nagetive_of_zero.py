# 2. Write a python script to check whether a given number is positive, negative or zero.


x = int(input("Enter a number: "))

match x:
    case x if x > 0:
        print("positive")
    case x if x < 0:
        print("negative")
    case 0:
        print("zero")


# print(f"the number {x} is",
#       "positive" if x > 0 else "negative" if x < 0 else "zero")
