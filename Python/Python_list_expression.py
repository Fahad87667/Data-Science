#List Compression 
# Syntax : 
# oldlist = []
# newlist = [expression(x) for x in oldlist if check]
result = []
for i in range(1,11):
    result.append(i)
    
print(result)
    
# How to do it with the help of List comprehension
result = [x for x in range(1,11)]
print(result)
# Get a list of all even numbers between 1 to 20

result = [x for x in range(1,21) if x % 2 == 0]
print(result)

# get all the odd numbers from  the given list
list1 = [1,2,4,5,4,3,6,7,9,13,5,6,4,6]
result = [x for x in list1 if x % 2 == 1]
print(result)
# convert all the str into upper case in given list
list2 = ['my','name','is', 'fahad']
result = [x.upper() for x in list2 ]
print(result)

# put all the negative numbers after positive numbers from given list
list3 = [1,-1,2,-5,9,10,-6]
# result1 = [x for x in list3 if x>0]
# result2 = [x for x in list3 if x<0]
result1 = [x for x in list3 if x>0] + [x for x in list3 if x<0]
print(result1)
 