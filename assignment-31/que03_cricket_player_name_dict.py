

# 3. Write a python script to create a dictionary where key values are cricket player names
# and data-values are tuple of 4 elements -matches played, total runs, half centuries
# and centuries. All data should be taken from user.

#                           matches played, total runs, half centuries, centuries
#     "Sachin Tendulkar":   (463,             18426,        96,           49), 
#     "Virat Kohli":        (254,             12169,        43,           43), 
#     "Rahul Dravid":       (344,             10889,        83,           12), 
#     "Sourav Ganguly":     (311,             11363,        72,           22), 
#     "Virender Sehwag":    (251,             8273,        38,           15),  
#     "MS Dhoni":           (350,             10773,        73,           10), 
#     "Yuvraj Singh":       (304,             8701,        52,           14),  
#     "Rohit Sharma":       (227,             9205,        43,           29),  
#     "Mohammad Azharuddin" (334,             9378,        58,           7),   
#     "Sunil Gavaskar":     (108,             10122,        31,           34)  

players = {}

while True:
    name = input("Enter players name (Enter exit for exit): ")
    if name == "exit":
        break
    tpl = tuple(input("Enter matches played, total runs, half centuries, centuries : ").split(" "))
    players[name] = tpl

print(players)