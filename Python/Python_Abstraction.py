# Oops abstraction 
# abstraction allows you to hide complex details and 
# focus on the essential aspects of your code, 
# making it more manageable and understandable, 
# especially as your codebase grows.

import abc
class Shape:  # Abstract class
    abc.abstractmethod
    def area(self):
        pass

    abc.abstractmethod
    def perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


circle = Circle(5)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())
