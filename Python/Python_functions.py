# Functions in python
# Examples of Inbuild functions --
a = [1,2,4,7,4,9]
print('sum = ', sum(a))
print('max = ', max(a))
print('min = ', min(a))
print('len = ', len(a))

# How do functions work
# They may or may not accepts input parameter
# They may or may not return any output
# def is a keyword to define a function '()'

# Example of a function which doesn't accept any parameter
def wish():
    print('Good Morning')
    
wish() # we have to call functions

# Example of a function which does accept any parameter
def message():
    return 'Good night'

print(message())
a = message()
print(a)

# Example of a function which accept any parameter
def avg_of_num(a,b):
    print(a)
    print(b)
    avg_result = (a+b)/2
    return avg_result
    
num1 = 34
num2 = 23
output = avg_of_num(num1,num2)
print(output)

# Write a function to calculate the factorial of a num

def factorial(a):
    result = 1
    for i in range(1,a+1):
        result *= i
    return result
    
num3 = 5
solution = factorial(num3)
print(f"Factorial of {num3} is = {solution}")

# How to return multiple values from functions

def sqr_and_cube(n):
    sqr = n*n
    cube = n*n*n
    return sqr,cube

num4 = 3
sqr,cube =  sqr_and_cube(num4)
print("Square = ",sqr)
print("Cube = ",cube)

# How to create optional arguments in python functions

def multiply(a, b=4):
    result = a*b
    return result

num5 = 2
num6 = 7

print(multiply(num5,num6))
print(multiply(num5))

# Non-Key valued arguments WE USE ARGS WHEN WE DONT KNOW THE LEN OF PARAMETERS
def example_nonkeyed_arguments( *argv ):
    for parameters in argv:
        print(parameters)
        
example_nonkeyed_arguments('Hello', 'Good Morning')

# Key value type of arguments in Python
def example_keyed_arguments(**kwargs):
    for k,v in kwargs.items():
        print(f"Key is {k} and Value is {v}")
        
example_keyed_arguments(hosts='172.34.34.34',port=7896, pswd='KJGJ')

# Using Map
def square(x):
    return x ** 2

a = [2,3,4,5,6]

b = list(map(square , a))
print(b)

square1 = lambda x: x ** 2
print(square1(3))

# How to work with map functions
list5 = [1,2,3,4,5,6,7,8]

# using lambda functions
squared = lambda x: x*x

square_list = list(map(squared, list5))
print(square_list)
