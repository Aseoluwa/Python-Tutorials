#DICTIONARIES
thisdict = {
    'brand':'Ford',
    'Model':'Mustang',
    'year':1964,
    'year':2000
}
print(type(thisdict))

print(thisdict['brand'])
print(thisdict['year'])
print(thisdict['Model'])

put = thisdict['Model']
put = thisdict['brand']
put = thisdict.get ('year')
print(thisdict)
print(put)

mariam = thisdict.keys()

mariam = thisdict.values()
print(mariam)

#to add a new item to the original dict

thisdict['Wheels'] = 'four wheek drive'
thisdict['Color'] = 'Red'
thisdict['Engine type'] = 'V6'
# thisdict.pop('Model')

print(thisdict)


#TO GET THE KEY AND VALUE PAIRS

temi = thisdict.items()
print(temi)

#TO CHECK IF A KEY EXSIST

if "Model" in thisdict:
    print("yes ,'Model' is valid")


list1 =  ["mariam", True, 'toss', 'love', 'damola', 'david', 1, 'temi'] 

print(len(list1))
print(type(list1))
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[-1])
print(list1[:4])   #OR print(list1[0:4])
print(list1[2:])    #OR print(list1[2:6])
print(list1[-4:-1])
print(list1[-8:-1 : 2])
print(list1[0:])



if 'mariam' in list1:
    print("yes, 'mariam' is in list1")

list1 =  ["mariam", True, 'toss', 'love', 'damola', 'david', 1, 'temi'] 
list2 =  ["BOLA", 'SMILE', 'BOSS','ASE'] 

tuple_faith = ['ogo', 'BOEE']

list1[1] = 'Faith'
print(list1)

list1[5:7] = ['salim', 'prof']
print(list1)

list1[-2] = 2
print(list1)

list1.insert(4,'ade')
print(list1)


list1.extend(tuple_faith)
print(list1)


list1.extend(list2)
print(list1)

#to list an item 

for i in range(len(list1)):
    print(list1[i])

[print(x) for x in list1]    


#while loop


i = 0

while i < len (list1):
    print(list1)
    i  = i + 1


# i = 0
# while i <10:
#     print(i)
#     i +=1

text = input('Input someting:')

print(text.strip())
print(text.split('.'))
print(text.upper())
print(text.capitalize())
print(text.lower())
