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

# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance


class Account:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number

    # For Checking The Balance
    def check_balance(self):
        print(self.balance)

    # For Debit
    def debit(self, amount):
        self.balance -= amount
        print(f"{amount} Debited Successfull New Balance {self.balance}")

    # For Credit
    def credit(self, amount):
        self.balance += amount
        print(f"{amount} Credit Successfull New Balance {self.balance}")


acc1 = Account(10000, 42201)
acc1.check_balance()
acc1.debit(5000)
acc1.credit(12000)
