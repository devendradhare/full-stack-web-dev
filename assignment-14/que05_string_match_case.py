# 5. Write a python script to take a string from the user. If the string is a part of "mysirg"
#    then print "One", if the string is a part of "education" then print "Two" and if the string
#    is a part of "services" then print "Three"

s = input("Enter a string : ")

match s:
    case s if s in "mysirg":
        print("One")
    case s if s in "education":
        print("Two")
    case s if s in "services":
        print("Three")
    case _ :
        print("no match")