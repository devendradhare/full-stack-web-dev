# 2. Write a python script to check whether a given number is divisible by 5 or not


x = int(input("Enter a number: "))
print(f"{x} is", "not divisible by 5" if x%5 else "divisible by 5")