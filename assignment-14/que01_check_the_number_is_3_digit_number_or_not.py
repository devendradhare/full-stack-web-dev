

# 1. Write a python script to check whether a given number is a three digit number or not.


a = int(input("Enter a number: "))

match a:
    case a if a > 99 and a < 1000:
        print("Number is a three digit number")
    case _:
        print("Number is not a three digit number")



# if a > 99 and a < 1000:
#     print("Number is a three digit number")
# else:
#     print("Number is not a three digit number")
