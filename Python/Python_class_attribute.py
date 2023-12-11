class Employee:
    
    count = 0
    # Constructor of class
    # it is mainly used for instance variables
    def __init__(self,name,salary): # {self is a pointer or current object ,point it to yourself or use to call}
        # Instance variable or instance attributes { attributes will be same but different values}
        self.emp_name = name
        self.emp_salary = salary
        Employee.count += 1
     
    #Method of a class    
    def displayEmployeeInfo(self):
        print("Employee name : ",self.emp_name, ", Employee Salary : ", self.emp_salary)
        
    def emp_count(self):
       print("Employee Count :", Employee.count)
        
emp1 = Employee('Fahad', 20000)

emp2 = Employee('Khan', 40000)


emp1.displayEmployeeInfo() # print(object.method())
emp1.emp_count()
emp2.displayEmployeeInfo()
emp2.emp_count()
print(emp1.emp_name,emp1.emp_salary)