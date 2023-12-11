# oops - Object oriented programming 
# Class:{ A blueprint or template for creating objects}. It defines attributes (characteristics) and methods (functions) that the objects of the class will have.
# Object: {An instance of a class}. It is a concrete entity created from the class, with specific values for its attributes.
# Attributes : Stores values for an object
# Behaviour: methods which shows the properties of a particular object

# How to create a class in python 
class Employee:
    # Constructor of class
    # it is mainly used for instance variables
    def __init__(self,name,salary): # {self is a pointer or current object ,point it to yourself or use to call}
        # Instance variable or instance attributes { attributes will be same but different values}
        self.emp_name = name
        self.emp_salary = salary
    
    #Method of a class    
    def displayEmployeeInfo(self):
        print("Employee name : ",self.emp_name, ", Employee Salary : ", self.emp_salary)
        
emp1 = Employee('Fahad', 20000)
emp2 = Employee('Khan', 40000) # These are objects of class

emp1.displayEmployeeInfo() # print(object.method())
emp2.displayEmployeeInfo()
print(emp1.emp_name,emp1.emp_salary)

# Define a class called Dog
class Dog:
    # Constructor (__init__) to initialize attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to make the dog bark
    def bark(self):
        print(f"{self.name} says Woof!")

# Create an instance of the Dog class
my_dog = Dog("Buddy", 3)

# Access attributes and call a method
print(my_dog.name)  # Outputs: Buddy
print(my_dog.age)   # Outputs: 3
my_dog.bark()       # Outputs: Buddy says Woof!

# Question 1: Create a Class and Objects
#Define a class named Rectangle with the following attributes: 
# length and width. Implement a method called calculate_area that calculates and returns the area of the rectangle.
# Create two instances of the Rectangle class and print their areas.

class Rectangle:
    def __init__(self,length,width):
        
        self.length = length
        self.width = width
        
    def calculate_area(self):
        return self.length*self.width
    
    def is_square(self):
        return self.length == self.width
        
            
rect1 = Rectangle(23,12)
rect2 = Rectangle(24,5)
rect3 = Rectangle(12,12)

area1 = rect1.calculate_area()
area2 = rect2.calculate_area()
area3 = rect3.calculate_area()

print("Area of Rectangle 1 =", area1)
print("Area of Rectangle 2 =", area2)
print("Area of Rectangle 3 =", area3)

# Checking if rectangles are squares and printing the result
print("Rectangle 1 is a square:", rect1.is_square())
print("Rectangle 2 is a square:", rect2.is_square())
print("Rectangle 3 is a square:", rect3.is_square())
        
'''Create a Python class called Book to represent information about books.
Each book should have attributes such as title, author, and publication_year.
Implement the following functionalities:

Initialize the Book class with the provided attributes.
Create a method display_info that prints the information about the book in a formatted way.
Add a class variable total_books to keep track of the total number of books created.
'''
class Book:
    total_books = 0
    def __init__(self,title,author,publication_year):
        
        self.title = title
        self.author = author
        self.publication_year = publication_year
        # class variable
        Book.total_books +=1
        
        
    def display_info(self):
        return (f'Name of the book -{self.title},  Name of the Author - {self.author},  Year of publication - {self.publication_year}')
    
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book2 = Book("Perks", "George Orwell", 1949)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

book1.display_info()
book2.display_info()
book3.display_info()

print(book1.display_info())
print(book2.display_info())
print(book3.display_info())
print(f"Total number of books = {Book.total_books}")
