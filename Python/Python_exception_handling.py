# How to handle exceptions in Python

# We use {try} syntax to check the error

a = 5

try:
    result = a/0
    print(result)
    
except ZeroDivisionError:
    print("Some error has occured")
    
b = [2,43,5,6,78,8,9]

try:
    result = (b[9])
    print(result)
    
# except Exception as err:
#     print(err)

except IndexError:
    print('Error')



# Use of else block  int try and except block
x = 5
try:
    result = x/0
    #result = x/5
except ZeroDivisionError:
    print('Error')
else:
    print(result)
    print("Calculation completed !!")
finally:
    print("Doesnt matter, try again!!!")    

# age = int(input("Enter your age: ")) 
# print(age)

# try:
#     age = int(input("Enter your age: "))
# except ValueError:
#     print("Invalid input. Please enter a valid number.")

