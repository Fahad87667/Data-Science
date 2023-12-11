# Acts like a map data structure 
# {
#     'keys' : 'Value' {keys are always in int, str format}
#     'name ': 'Fahad'
#     'age' : 20
# }
dict1 = {}
print(dict1)
# How to insert values in dictionry
dict2 = {}
dict2['Name'] = 'Fahad'
dict2['Age'] = 20
dict2[34] = 'Randome key'
dict2['Other_details'] = {'Nationality' : 'Indian', 'Religion' : 'Islam'}

print(dict2)
print(len(dict2))
#access
print(dict2['Name']) # to access syntax is {print(dict[key])}
print(dict2['Other_details']['Nationality'])

#update 
dict2['Age'] = 30
print(dict2['Age'])

# How to get the keys from a dictionary
total_keys = list(dict2.keys())
print(total_keys)

# How to get the values from a dictionary
total_values = list(dict2.values())
print(total_values)

# How to iterate on dictionary
for k,v in dict2.items():
    print('key is =', k,'and Value is =', v)
    
# Compare dictionary 

dict3 = {'a':1, 'b':2, "c":4}
dict4 = {'c':1, 'a':1, "b":2}

print(dict3 == dict4)

# How to delete specific key value pair from dictionary
# del dict[]

# How tp check if Value exists in dictionary or not
print(dict2.get('Age'))

# How to check if Key exists in dictionary or not
keys_indict = list(dict2.keys())
if 'Age' in keys_indict:
    print(True)
else:
    print(False)
    