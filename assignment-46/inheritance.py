

# 1. Define a class Person with instance object variables name and age. Provide
#    __init__() method to set instance object variables. Also define methods to show
#    name and age. Now define a subclass Employee of Person with instance object
#    variable salary. Provide __init__() method to initialise instance object variable. Also
#    define instance method to show Employee data.
class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def show_name(self):
        print("Name:", self.name)

    def show_age(self):
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name=None, age=None, salary=0):
        self.salary = salary
        super().__init__(name, age)

    def show_Employee(self):
        self.show_name()
        print("salary:", self.salary)
        self.show_age()


e = Employee("devendra dhare", 20, 5000000)
# e.show_Employee()


# 2. Define a class Account with instance object variables accountNo, balance and static
#    variable rate_of_interest. Provide needful methods. Define subclass FixedDeposit
#    of Account class with instance object variable time. Provide setter and getter. Also
#    define a method to calculate simple interest.
class Account:
    rate_of_interest = 5

    def __init__(self, accountNo=None, balance=None):
        self.accountNo = accountNo
        self.balance = balance

    def set_accountNo(self, accountNo):
        self.accountNo = accountNo

    def get_accountNo(self):
        return self.accountNo

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def set_rate_of_interest(self, rate):
        Account.rate_of_interest = rate

    def get_rate_of_interest(self):
        return Account.rate_of_interest


class FixedDeposit(Account):
    def __init__(self, accountNo=None, balance=None, time=None):
        super().__init__(accountNo, balance)
        self.time = time

    def set_time(self, time):
        self.time = time

    def get_time(self):
        return self.time

    def calculate_interest(self):
        return (self.get_balance() * self.get_rate_of_interest() * self.get_time()) / 100


fd = FixedDeposit()
fd.set_accountNo("FD001")
fd.set_balance(10000)
fd.set_time(2)

interest = fd.calculate_interest()
# print(interest)  # Output: 1000.0


# 3. Demonstrate the use of super() in inheritance.
class A:
    def world(self):
        print("world")


class B(A):
    def hello(self):
        print("hello")
        super().world()


a = B()
# a.hello()


# 4. Define a class Account with instance object variable balance with initial value as O.
#    Provide withdraw and deposit methods. Now define a subclass
#    MinimumBalanceAccount of Account with provided minimum balance. Override
#    withdraw method according to minimum balance condition.
class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def get_balance(self):
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ₹{amount} successfully.")
            print("Current balance:", self.balance)
        else:
            print("Insufficient balance.")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount} successfully.")
        print("Current balance:", self.balance)


class MinimumBalanceAccount(Account):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print(
                f"The balance after withdrawal should not go below ₹{self.min_balance}.")
        else:
            super().withdraw(amount)


# # Create an instance of Account
# account = Account()

# # Deposit some funds
# account.deposit(2000)

# # Withdraw some funds
# account.withdraw(1500)

# # Create an instance of MinimumBalanceAccount
# min_balance_account = MinimumBalanceAccount(3000, 2000)

# # Deposit some funds
# min_balance_account.deposit(4000)

# # Withdraw some funds
# min_balance_account.withdraw(3500)


# 5. Define a class Polygon with instance object variable to store number of sides and a
#    list of n side length values. Define a subclass Triangle of Polygon with instance
#    methods getArea().
class Polygon:
    def __init__(self, sides, lengths):
        self.sides = sides
        self.lengths = lengths

    def get_area(self):
        raise NotImplementedError("Subclasses must implement this method.")


class Triangle(Polygon):
    def get_area(self):
        if self.sides == 3:
            a, b, c = self.lengths
            s = (a + b + c) / 2  # Calculate the semi-perimeter
            # Calculate the area using Heron's formula
            area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
            return area
        else:
            raise ValueError("A triangle must have exactly 3 sides.")


triangle = Triangle(3, [3, 4, 5])
area = triangle.get_area()
print("Area of the triangle:", area)
