

# 3. Write a python script to count vowels in a given string.

s = input("Enter a string : ")

print("vowels in that string\n",
      "\na =", s.count('a')+s.count('A'),
      "\ne =", s.count('e')+s.count('E'),
      "\ni =", s.count('i')+s.count('I'),
      "\no =", s.count('o')+s.count('O'),
      "\nu =", s.count('u')+s.count('U'))
