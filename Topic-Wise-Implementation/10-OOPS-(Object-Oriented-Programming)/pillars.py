# Abstraction
# Hiding the implementation details of a class and only showing the essential features to the user
# for example i have a car and i need to start it so if i start the car i did not see the car machenism or process of starting a car because it is done internally so the process is hidden and if any implementation is hidden it is called as abstraction


class Car:
    def __init__(self):
        self.acc = False
        self.clutch = False
        self.brk = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car is Started....")

    @staticmethod
    def stop():
        print("Car Stopped.....")


Car().start()  # SO The clutch and acc are changing into true when car is started but it is hidden user cannot see it

# Encapsulation
# Wrapping data and functions into a single unit (object)

car = Car()
print(car.brk)

# del car
# print(car) # NameError: name 'car' is not defined. Did you mean: 'Car'?

# Private(like) attributes & methods

# Conceptual implementation in python

# Private attributes and methods are meant to be used only within the class and are not accessible from outside the classs


class Account:
    def __init__(self, account_number, account_password):
        self.account_number = account_number
        self.__account_password = account_password


acc = Account(1234, "abcd")

print(acc.account_number)
# print(acc.__account_password)

# Inheritence
# when one class (child/derived) derives the properties & methods of another class (parent/base)


class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand


car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")
car1.start()  # prints because it is inherited
print(car1.brand, car2.brand)

# Types
# Single Inheritence
# Multi-level Inheritence
# Multiple Inheritence


class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type


f1 = Fortuner("Diesel")
f1.start()


# multiple inheritence
class A:
    varA = "This is class A"


class B:
    varB = "This is class B"


class C(A, B):
    varC = "This is class C"


c1 = C()
print(c1.varA)


# Super method
# is used to access methods from parents
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name):
        super().__init__(name)


s = Student("Ammar")
print(s.name)

# @classmethod decorator
# A class method is bound to the class & receives the class as an implicit 1st argument
# Note: static method can't access or modify the class state & generally for utility


class People:
    name = "Unknown"

    # def change_name(self, name):
    #     self.name = name
    #     Person.name = name
    #     self.__class__.name = name

    @classmethod
    def change_name(cls, name):
        cls.name = name


p1 = People()
p1.change_name("Umar")
print(p1.name)
print(People.name)


# property decorator
class Stu:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3)


stu1 = Stu(98, 97, 99)
print(stu1.percentage)

stu1.math = 10
print(stu1.percentage)

# Polymorphism : Opearator Overloading
# when the same opearator is allowed to have different meaning according to the context


class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def showNumber(self):
        print(f"{self.real}i + {self.imaginary}j")

    # def add(self, num2):
    #     new_real = self.real + num2.real
    #     new_imaginary = self.imaginary + num2.imaginary
    #     return Complex(new_real, new_imaginary)

    # opearators and dunder functions (function which has __ is called dunder functions)
    
    def __add__(self, num2):
        new_real = self.real + num2.real
        new_imaginary = self.imaginary + num2.imaginary
        return Complex(new_real, new_imaginary)

    def __sub__(self, num2):
        new_real = self.real - num2.real
        new_imaginary = self.imaginary - num2.imaginary
        return Complex(new_real, new_imaginary)


c1 = Complex(5, 10)
c1.showNumber()

c2 = Complex(10, 10)
c2.showNumber()

c3 = c1 + c2
c4 = c1 - c2
c3.showNumber()
c4.showNumber()
