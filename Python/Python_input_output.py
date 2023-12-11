# Declare and assign variables in python
int_var = 10
float_var = 10.78
string_var = 'Hello brother'

bool_var = True # or False

#Functions
print('Value of int =', int_var, '-- result done')

#to check the data type of any variable in python we can use
#type() function
print('type of first variable', type(int_var))
#how to do type casting
#int(), float(), str(), bool()
int_var = int_var + 10
int_var = float(int_var)
print('int to float = ', int_var)

# type casting
numeric_str = "123"
numeric_str = int(numeric_str) + 50

print("Typecasted value of numeric str is ",numeric_str)

# How to take inputs in python?
# we can use input() function
#name = input()
#age = input()

#print('User name =',name)
#print('User age =',age)

# Another way to take user input with custom message

''' name = input("Enter your first name :-")
last_name = input('Enter your last name :-')

 print('Full Name',name, last_name)'''

# Concatination is when we add two strings
str1 = "Fahad "
empty_str= ''
str2 = 'Khan'

print(str1 + empty_str+ str2)