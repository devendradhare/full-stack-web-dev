# 4. Write a python script to check whether a given year is a leap year or not.


x = int(input("Enter a year: "))
if x % 4 == 0:
    if x % 100 == 0:
        if x % 400 == 0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")
