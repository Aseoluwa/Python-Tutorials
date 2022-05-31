#TO WRITE A TEXT FILE

file = open('someone.txt', 'w')

write = file.write('Aeyy') 

print(write)

#or

file = open ('someone.txt','w')

file.write('heyy\nmy\nis ase') 
file.close()

#CHAIN CONDITIONALS( AND / OR)

x = 2

y = 3

if x == y and x+y == 5:

    print('Worked1')
if x == y or x+y == 5:

    print('Worked')
    if x == y and x+y == 5:

        print('Working')

        if y == x or x+y ==5 and y-x == 1:

            print('run')
if not ( x==y or x+y ==6):  
    print('Work')         
            

else:
    print('G😒 😒 D MORNING')


#EXAMPLE2

if x == 2:
    print('correct!')
    if y == 3:
        print('x=2, y=3')
    else:
        print('x=2. y!=3')    
else:
    print(x!=2)    


#COLLCETION DATA TYPES

#LIST  (Can duplicate )
list1 = ['apple', 'samsung','redmi','infinix', 'tecno','redmi']

#SET
set1 = ['apple', 'samsung','redmi','infinix', 'tecno']

#DICTIONARIES
thisdict = {
    'brand':'Ford',
    'Model':'Mustang',
    'year':1964
}
print(type(thisdict))
#TRIPLE (Can duplicate )
trp_1 = ('apple', 'samsung', 'redmi', 'infinix', 'redmi', 'tecno')

print(trp_1)

#FOR LOOPS(Start, stop, steps (by default +1))

# for x in range (1, 11):

#     print (x)

   #OR    

for y in range (0, 10,2):
    print (y)

print(len(trp_1))


#to convert tup_1 to a list and remove a word form a list

convert = list(trp_1)
print(convert)

convert.remove('apple')
print(convert)

#to add to a list

convert.insert(4,'nokia')
print(convert)
print('sam' in convert)

#STRING MRTHODS

string1 ="Temiloluwa"
print(string1.find('e'))
print(string1.find('ilo'))
print(string1.count('l'))


#EXAMPLE

# password = input ('Please Type in your password:')
# if password.count('_') >0:
#     print('STRONG PASSWORD')

# else:
#     print('Try again')   

#Eg 2     
# password = input ('Please Type in your password:')
# if password.isupper():
#     print('STRONG PASSWORD')    

# else:
#     print('Try again')  

# if password.isnumeric():
#     print('Strong Number')    

#SET
set1 = {'Shege', 'Mariam', 'Dave', 'Damola'} 
set2 = {'Shege', 'Dave'}

print(set1)

#CONVERTING TO A LIST

name = list(set1)
print(name)

print(len(set1))

set1.add('oba')
print(set1)

## add is a set method

set1.discard('Dave')
print(set1)

newset = set1.difference(set2)
print(newset)
newset = set1.union(set2)
print(newset)

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

#Mariam = thisdict.keys()

mariam = thisdict.values()
print(mariam)

#to add a new item to the original dict

thisdict['Wheels'] = 'four wheek drive'
thisdict['Color'] = 'Red'
thisdict['Engine type'] = 'V6'
thisdict.pop('Model')

print(thisdict)


