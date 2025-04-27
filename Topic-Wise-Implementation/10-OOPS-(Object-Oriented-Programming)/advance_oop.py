# Create a class Animal:

# Attributes: name, species

# Methods:
# A constructor to initialize these attributes.
# A method speak() that prints a generic sound for animals.

# Now, create two subclasses:
# Dog and Cat that inherit from Animal.
# Override the speak() method in both subclasses to print the respective sounds (e.g., "Woof" for dogs and "Meow" for cats).


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print("Generic animal sound")


class Dog(Animal):
    def speak(self):
        print("Woof")


class Cat(Animal):
    def speak(self):
        print("Meow")


Dog("Dog", "Dog").speak()
Cat("Cat", "Cat").speak()
