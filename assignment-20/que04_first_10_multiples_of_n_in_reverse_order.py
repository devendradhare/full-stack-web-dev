

# 4. Write a python script to print the first 10 multiples of N in reverse order.

n = int(input("Enter a number: "))

for i in range(n*10, n-1, -n):
    print(i,end=" ")