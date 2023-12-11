# class Book:
#     #class attribute
#     total_books = 0
#     def __init__(self,title,author,publication_year):
        
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year
#         # class variable
#         Book.total_books +=1
        
        
#     def display_info(self): #Method
#         return (f'Name of the book -{self.title},  Name of the Author - {self.author},  Year of publication - {self.publication_year}')
    
# book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
# book2 = Book("Perks", "George Orwell", 1949)
# book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

# book1.display_info()
# book2.display_info()
# book3.display_info()

# print(book1.display_info())
# print(book2.display_info())
# print(book3.display_info())
# print(f"Total number of books = {Book.total_books}")

# # Print instance variable of an object
# print(book1.author)
# print(book1.title)
# print(book1.publication_year)

# # Lets access Class variable from instance itself

# book2.author = 'Stephen Chbosky' # Updated variable using instance

# print(book2.author)
# print(book2.display_info())
                                                        
# What is static method
class Car:
    
    def __init__(self, name, color):
        self.name = name
        self.color = color 
        
    def displayinfo(self):
        print('Car name is ->', self.name, 'with ', self.color, 'color')
        
    @staticmethod #They are called on the class itself rather than on an instance   
                  # Dont need to make objects ,we can directly run from class using staticmethod
    def initialMessage(): 
        print("Nice Car !!!")
        
        
Car.initialMessage()       

car1 = Car('Mercedes',"Black")
car2 = Car('BMW','Red')

car1.displayinfo()
car2.displayinfo()
print(car1.name)  

# This will not work
# Car.displayinfo() 

#Using only static method
class student:
    @staticmethod
    def uniform():
        print("Students should wear thier respective uniform") 
        
student.uniform()    

class Calculator:
    @staticmethod
    def sum( x,y ):
        print(x + y)
    
    def minus(x,y):
        print(x-y)
        
    def multiply(x,y):
        print(x*y)
        
    def square(x):
        print(x**2)
        
    def cube(x):
        print(x**3)
    
Calculator.sum(67,34)
Calculator.minus(40,20)
Calculator.multiply(8,9)
Calculator.square(15)
Calculator.cube(9)