# 1. Define a Python class Person with name and age as instance object variables.
# Define Student and Teacher two subclasses of Person. Provide rollNo as instance
# object variable in Student, provide subject as instance object variable in Teacher
# class. Now define a function show to print values of instance object variables in
# both the classes. Demonstrate polymorphic behaviour or show function.
class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age


class Student(Person):
    def __init__(self, name=None, age=None, rollNo=None):
        super().__init__(name, age)
        self.rollNo = rollNo

    def set_rollNo(self, value):
        self.rollNo = value

    def get_rollNo(self):
        return self.rollNo

    def show(self):
        print("Roll no. :", self.rollNo, "\nname:",
              self.name, "\nage:", self.age)


class Teacher(Person):
    def __init__(self, name=None, age=None, subject=None):
        super().__init__(name, age)
        self.subject = subject

    def set_subject(self, subject):
        self.subject = subject

    def get_subject(self):
        return self.subject

    def show(self):
        print("name:", self.name, "age:", self.age, "subject:", self.subject)


t = Teacher("anita bhade", 30, "physics")
s = Student("devendra dhare", 20, 12345678)
# t.show()
# s.show()

# 2. Overload greater than (>) operator in Tme class which has instance object
# variables hour, min, sec.


class Tme:
    def __init__(self, hour, min, sec):
        self.hour = hour
        self.min = min
        self.sec = sec

    def __gt__(self, other):
        if self.hour > other.hour:
            return True
        if self.min > other.min:
            return True
        if self.sec > other.sec:
            return True
        return False


t1 = Tme(7, 7, 7)
t2 = Tme(7, 7, 2)
# print(t2>t1)


# 3. Define a class Result to hold result data for a test (attempt, right and wrong).
# Overload + operator to combine the result of two tests.
class Result:
    def __init__(self, attempt=0, right=0, wrong=0):
        self.attempt = attempt
        self.right = right
        self.wrong = wrong

    def show(self):
        print("attempt:", self.attempt, "\nright",
              self.right, "\nwrong:", self.wrong)

    def __add__(self, other):
        return Result(self.attempt+other.attempt, self.right+other.right, self.wrong+other.wrong)


t1 = Result(10, 7, 3)
t2 = Result(15, 7, 8)
# (t1+t2).show()

# 4. Define a class matrix with member variables rows, columns and a list to hold matrix
# elements. Overload + operator to add two matrix objects.


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            print("rows and columns do not match")
            raise ValueError("rows and columns do not match")

        temp = []
        for i in range(self.rows):
            lst = [self.matrix[i][j] + other.matrix[i][j]
                   for j in range(self.columns)]
            temp.append(lst)
        return Matrix(temp)

    def __sub__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            print("rows and columns do not match")
            raise ValueError("rows and columns do not match")

        temp = []
        for i in range(self.rows):
            lst = [self.matrix[i][j] - other.matrix[i][j]
                   for j in range(self.columns)]
            temp.append(lst)
        return Matrix(temp)

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            print("rows and columns do not match")
            raise ValueError("rows and columns do not match")

        temp = []
        for i in range(self.rows):
            lst = [self.matrix[i][j] + other.matrix[i][j]
                   for j in range(self.columns)]
            temp.append(lst)
        return Matrix(temp)

    def show(self):
        for i in self.matrix:
            print(i)


m1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

m2 = [[9, 8, 7],
      [6, 5, 4],
      [3, 2, 1]]

mtx1 = Matrix(m1)
mtx2 = Matrix(m2)
mtx1.show()
print()
mtx2.show()
print()
(mtx1+mtx2).show()
print()
(mtx1-mtx2).show()


# 5. In Question 4, define - operator to subtract two matrix objects.
