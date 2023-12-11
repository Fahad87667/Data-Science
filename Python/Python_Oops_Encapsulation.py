'''
Encapsulation means Binding attributes and methods together
Inheritence--{ is the capability of one cl;ass to derive or inherit the properties 
from another class}
'''
class car:
    def __init__(self, year, make, model, speed):
        #  We hide the constructor in using "__" syntax before attributes
        # These are private attributes
        self.__year = year
        self.__make = make
        self.__model = model
        self.__speed = 0
    
    def set_speed(self,speed):
        self.__speed = 0 if speed < 0 else speed
        
    def get_speed(self):
        return self.__speed 
    
           
        
c = car(2020, "Mercededs", "benz", 0)
print(c._car__make)

c.set_speed(-67)
print(c.get_speed())


c.set_speed(28)
print(c.get_speed())

class BankAccount:
    def __init__(self, balance=0):
        # Private attribute
        self._balance = balance

    # Getter method for balance
    def get_balance(self):
        return self._balance

    # Setter method for balance
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid deposit amount.")

    # Setter method for balance with additional checks
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")


# Creating an instance of the BankAccount class
account = BankAccount(1000)

# Accessing the balance using the getter method
print("Initial balance:", account.get_balance())

# Depositing and withdrawing funds using methods
account.deposit(500)
account.withdraw(200)
account.withdraw(1000)  # Invalid withdrawal amount

 


