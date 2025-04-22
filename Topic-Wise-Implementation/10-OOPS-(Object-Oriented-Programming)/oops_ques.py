# Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        sum = 0
        if isinstance(self.marks, list):
            for mark in self.marks:
                sum += mark
            average = sum / len(self.marks)
        return average


s1 = Student("Umar", [98, 99, 97])
print(s1.calculate_average())
