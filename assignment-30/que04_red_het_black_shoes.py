

# 4. You have a list of names of candidates, some of them are wearing black hat, some
# of them are wearing red shoes and some of them are wearing both. Now you have
# given a list of names of candidates wearing black hat. There is another list of names
# of candidates wearing red shoes. Write a python script to find out the names of the
# candidates wearing black hat and red shoes.


black_hat = set(["devendra", "ram", "codendra", "rahul", "akshay"])
red_shoes = set(["binod", "ajay", "nayka", "devendra", "ram"])

print(black_hat.intersection(red_shoes))
