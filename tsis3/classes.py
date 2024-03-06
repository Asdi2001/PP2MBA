#1
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = raw_input()

    def print_string(self):
        print self.s.upper()

str_obj = InputOutString()
str_obj.get_string()
str_obj.print_string()

#2
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length):
       self.lenght = length
    def area(self):
        return self.length * self.length
    
#3
class Rectangle(Shape):
    def __init__(self, length, width):
       self.length = length
       self.width = width
       
    def area(self):
       return self.length * self.width

#4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, x1, y1):
        self.x = x1
        self.y = y1

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
    
#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(amount, self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal")
        else:
            self.balance -= amount
            print(amount, self.balance)

account = Account("John Doe")

account.deposit(1000)
account.withdraw(500)
account.withdraw(700)

#6
def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(lambda x: prime(x), numbers))
print(prime_numbers)
