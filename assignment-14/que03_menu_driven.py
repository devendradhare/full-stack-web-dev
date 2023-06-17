
# 3. Write a python script to make a menu driven program in which user has to choose
#    one of the option from four given options - 1) Odd-Even, 2) positive - Non Positive, 3)
#    Simple Interest and 4) find roots of quadratic equation. Match and execute
#    appropriate code on user selection.
print("menu driven program")
print("Enter 1 for Odd-Even", "Enter 2 for Positive - Non Positive", "Enter 3 for Simple Interest", sep="\n")
i = int(input())

match i:
    case 1:
        print("Even-Odd")
        x = int(input("Enter a number : "))
        print("Even" if x%2==0 else "Odd")
    case 2:
        print("positive - non-positive")
        x = int(input("Enter a number : "))
        print("Positive" if x > 0 else "non-positive")
    case 3:
        print("Simple Interest")
        p = float(input("Enter Principal amount : "))
        r = float(input("Enter interest rate    : "))
        t = float(input("Enter Time             : "))
        si = (p*r*t)/100
        print("Simple Interest =", si)
    case _:
        print("Invalid choice")







