

# 3. Write a python script to print first M multiples of N.



x = int(input("Enter a number: "))
y = int(input("how many multiples you want to print: "))

for i in range(x, x*y+1, x):
    print(i)