# how to use if else in python'

x = 10 
y = 5

if x>y :
    print('WOWW!!')
else:
    print('NO')
    
# Its not mandatory to use else always.

a = 10 
b = 3

if a == b :
    print('yes its equal')
    
print('BYE !!')  

'''
Nested If-Else conditions
Question :- 
marks = 90 
conditions , marks >= 90 -- A
             marks >=80 and marks <90-- -B
             marks >=70 and marks <80--- C
             
             
LOGIC :-

if c1(condition 1):
    s1(condition 2)
elif c2:
    s2
else:
     s3
''' 
m = 96

if m > 90:
    print('A')
    
elif m >=80 and m < 90:
    print('B')
        
elif m >= 70 and m < 80:
    print('C')

else :
        print('fail')
    
