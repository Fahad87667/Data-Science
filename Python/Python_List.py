# Lists in python 
# It stores heterogempous kind of data
# Sequenitial data
# Stored in contiguous memory locations
# Syntax 
# l1 = []
l1 = []
print(len(l1))
# Insert values in list
l1.append(5) #APPEND = Add element to the end of a list or array.
l1.append(7)
l1.append(9)

print(l1)

# Create a list of 1000 numbers start from 1 to 1000

# int_list = []
# for i in range(1,101):
#     int_list.append(i)
#     print(int_list)

# Calculation of  length of the list
len_of_list = len(l1)
print(len_of_list)

# how to check whether lists are equal or not
# l2 = [2,4,5]
# l3 = [9,0,2]
# print(l2 == l3)

# lists concatination
l2 = [2,4,5]
l3 = [9,0,8]
result = l3 + l2
print(result)

# How to access list values
l4 = [3,4,5,6,7]
print(l4[2])

# updating elements in lists
l4[2] = "Fahad"
print(l4)

#How to print list elements using length 
for i in range(1, len(l4)): # len{} = index notation
    print(l4[i])
    
# Difference between apppend and extend()
#APPEND
l5 = [1,13,34,'FAHAD', 78]
l6 = [4,7,0,6]
l5.append(l6)
print(l5)
print(len(l5))
# EXTEND
l5 = [1,13,34,'FAHAD', 78]
l6 = [4,7,0,6]
l5.extend(l6)
print(l5)
print(len(l5))

# List Slicing
list7 = [45,43,67,99,23,65,87,35,32,2,4]
# Syntax --> list_name[start : end]
print(list7[  :  ])
print(list7[ 1 : 4 ])
print(list7[ 5 :6  ])
# negative index -1 means last element of the list
# reverse the list
print(list7[-1 :: -1]) 