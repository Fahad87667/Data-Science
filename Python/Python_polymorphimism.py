
# Polymorphimism :- same representation but different definition 
#In Python, 
# polymorphism refers to the ability of different objects to be used 
# interchangeably,allowing a single function, method, or operator to work with 
# objects of various types or classes.






# Function overriding in python

from math import pi

class shape:
   def __init__(self,name):
       self.name = name
       
   def area(self):
       pass
   
   def fact(self):
       pass
   
   
   def whichshape(self):
       print(self.name)
       
       
class Square(shape):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length
    
    def area(self):
        print(self.length**2)
        
    def fact(self):
        print("Square has each side equal")
        
class Circle(shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        print(pi * self.radius**2)
   

sq = Square('SQUARE',5)
O = Circle('Gola',5)

sq.area()
O.area()

O.whichshape()
sq.whichshape()

sq.fact()
O.fact()  # empty line no execution no output