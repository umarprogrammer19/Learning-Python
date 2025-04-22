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


Car().start()  # SO The clutch and acc are changing into true when car is started but it is hidden user cannot see it

# Encapsulation
# Wrapping data and functions into a single unit (object)
