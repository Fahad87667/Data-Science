'''
Looping:
For loop -> When number of iterations are known.
While loop -> When number of iterations are unknown.

For Loop :- 
for i in range(1,11[HERE 11 IS EXCLUSIVE because indexing starts from 0th position]):{its the function that accepts parameters}
print(i)
'''
#WRITE A CODE TO PRINT NUMBERS FROM 1 TO 10

for num in range(1,11):
    print(num)
    
# write a code to print numbers from 1 to 11 in every 2 steps 
# odd numbers
for num in range(1,11,2):#{now we add the 3rd parameter as an incremental steps value as it will take this number of steps to continue loop }
    print(num)
    
# print numbers from 10 to 1
for num in range(10,0,-2):
    print(num)
    
# Write a program to calculate the sum ofgiven list elements using for loop
int_list = [4,8,-2,10,5]
list_sum = 0

for num in int_list:
    list_sum = list_sum + num
print('Sum of the loop is',list_sum) 