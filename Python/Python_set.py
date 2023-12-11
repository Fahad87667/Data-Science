# Sets in python
# set1 = set() # Empty set but if you use set1 = {} it'll show empty dict
# print(type(set1))

list1 = [1,2,3,4,1,2,4,6,3,27,8,3,4]
set1 = set(list1)
print(set1)

set2 = {1,3,4,5,5,7,8,2,4,6,2}
print(set2)

# How to iterate elements in the set
for num in set2:
    print(num)
    
# Convert output of set into lists
set3 = list(set2)
print(set3)
print(set3[-1])

# How to insert elements in the set
set4 = set()
set4.add(2)
set4.add(2)
set4.add(3)
set4.add(4)
set4.add(5)
set4.add(5)
print(set4)

# Use of update method
tmp = [1,2,3,4,3,4,3,3,2,5,6,7]
set4.update(tmp)
print(set4)

# Calculate the length of set
print(len(set4))

# set operations
set5 = {1,3,4,5,4,5,4,7,8,9,6}
set6 = {2,4,5,8}

#union operation 
print(set5 | set6)

#intersecton operation
print(set5 & set6)