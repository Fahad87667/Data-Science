# Inheritence in Python
# class me subclass parent class me child class

# Base class aka parent class
class Person:
    def __init__(self, name):
        self.name = name

    def displayname(self):
        print(self.name)

    # By defaulting we can say that a particular person is unemployed
    def isEmployed(self):
        print(self.name, "is Unemployed !!")


# Derived class aka child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, designation):
        # Call the __init__ method of the base class (Person) using super()
        super().__init__(name)
        self.idnumber = idnumber
        self.salary = salary
        self.designation = designation

    def isEmployed(self):
        print(self.name, "is Employed !!")


# Creating an instance of the Employee class
emp1 = Employee('Fahad', '123', 50000, 'Data Engineer')

# Accessing attributes of the Employee class
print(emp1.name)
print(emp1.idnumber)
print(emp1.salary)
print(emp1.designation)

# Calling methods of the Employee class
emp1.displayname() 
emp1.isEmployed()
