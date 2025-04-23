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
    def __init__(self, name):
        self.name = name


car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")
print(car1.name, car2.name)
car1.start()  # prints because it is inherited
