# 4. Write a python script to take one data from user and evaluate the type of data. If the
#    data is of int type then print Monday, if the data is of float type then print Tuesday, if
#    the data is of complex type then print Wednesday, if the data is of type bool then
#    print Thursday.

x = eval(input("Enter a type of data: "))

match x:
    case x if type(x) == int:
        print("Monday")
    case x if type(x) == float:
        print("Tuesday")
    case x if type(x) == complex:
        print("Wednesday")
    case x if type(x) == bool:
        print("Thursday")
    case _ :
        print("other type of data")