# 4. Write a python script to convert a str type data into an int type.
#    Also describe when a str type value is not possible to convert into an int type.


s = "1234"
print("s =", s, "       type =", type(s))
print("after conversion")
s = int(s)
print("s =", s, "       type =", type(s))

s = "123DVN"
s = int(s)      # this will generate a error