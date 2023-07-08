

# 1.  Define a python class Person with instance object variables name and age. Set
#     Instance object variables in __init__ () method. Also define show() method to display
#     name and age of a person.
class Person:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("neme: ", self.name, "\nage:", self.age)


# dvn = Person("Dvn", 20)
# dvn.show()


# 2.  Define a class Circle with instance object variable radius. Provide setter and getter
#     for radius. Also define getArea() and getCircumference() methods.
class Circle:
    def __init__(self, r):
        self.radius = r

    def set_radius(self, r):
        self.radius = r

    def get_radius(self):
        return self.radius

    def getArea(self):
        return (22/7)*self.radius**2

    def getCircumference(self):
        return 2 * (22/7) * self.radius


crl1 = Circle()
crl1.set_radius(10)
# print("radius:", crl1.get_radius())
# print("area:", crl1.getArea())
# print("circumference:", crl1.getCircumference())

# 3.  Define a class Rectangle with length and breadth as instance object variables.
#     Provide setDimensions(), showDimensions() and getArea() method in it.


class Rectangle:
    def setDimentions(self, a, b):
        self.length = a
        self.width = b

    def showDimentions(self):
        print("length =", self.length, "width =", self.width)

    def getArea(self):
        return self.length * self.width


rct = Rectangle()
rct.setDimentions(4, 5)
# rct.showDimentions()
# print(rct.getArea())


# 4.  Define a class Book with instance object variables bookid, title and price. Initialise
#     them via __init__( ) method. Also define method to show book variables.
class Book:
    def __init__(self, book_id=None, title=None, price=None):
        self.bookid = book_id
        self.title = title
        self.price = price

    def show_book(self):
        print("book ID: ", self.bookid, "\nbook Title: ",
              self.title, "\nprice: ", self.price)


dvn_book = Book(1234, "learn python", 499)
# dvn_book.show_book()


# 5.  Define a class Team with instance object variable a list of team member names.
#     Provide methods to input member names and display member names.
class Team:
    player_list = []

    def add_player(self, name):
        self.player_list.append(name)

    def display(self):
        print(self.player_list)


t20 = Team()
t20.add_player("asdf")
t20.add_player("qwer")
t20.add_player("kgdnv")
t20.add_player("qowir")
t20.display()
