# numerical operarions
""" + for addition
i for substraction
* for multiplication
/ for float division
// for integer devision
** for power calculation 2**3 =2*2*2
% for modulus
"""

x = 4
y = 3

print(x+y)
print(x-y)
print(x/y)
print(x//y)
print(x*y)
print(x%y)
print(x** y)

''' ASSIGNMENT OPERATORS
x += 5, = x = x + 5
x -= 5, = x = x - 5
x *= 5, = x = x * 5
x /= 5, = x = x / 5
x //= 5, = x = x // 5'''

'''COMPARISON OPERATORS always gives boolean values
== , Equals to condition , a == b
!= , Not Equals to condition , a != b
'''
a = 10
b = 5
print('comparing a and b ', a != b)
print('comparing a and b ', a == b)
print('comparing a and b ', a > b)
print('comparing a and b ', a < b)
print('comparing a and b ', a >= b)

'''
Logical operators in python ;- logical check will happen for expression result
and -> Returns true if both statements are True
or ->  Returns true if  one of the statements are True
not -> Reverse the result , returns false if the result is true
'''

a = 9
b = 3

print(a>4 and b<9)
print(a>90 or b>9)
print(not(a<8 and b<9))

