#BASIC COMPARISON OPERATORS
# >
# <
# ==
# !=

# print(2 == 4)
# print(2 != 4)
# print(2 < 4)
# print(2 > 1.4 * 3)
# print(2 - 3 + 4 > 5 - 29 * 42-30)

# print(len('hello'))

# print(True > False)

#TO READ A FILE FROM A TXT PG
# file = open('someone.txt', 'r' )
# f = file.readlines()

# print(f)

# newList =[]
# for line in f:
#     if line [-1] == '\n':
#         newList.append (line[:-1])

#     else:
#         newList.append(line)

# print(newList)

# OR 

# newList = []
# for line in f:
#    newList.append (line[:-1])

# print(newList)


#OR STRIP METHOD

file = open('someone.txt', 'r')

f = file.readlines()

newList = []
for line in f:
     newList.append(line.strip())

print(newList)






sHola = 72
Funke = 22

if Funke > sHola:
    print('Funke is greater than sHola')

else:
    print('Funke is greater than Shola')

print (bool('Hello'))    
print(bool(0.019))
print(bool())

g = 'hello'

h = '-0.19'

# print(bool !=(g))
# print(bool('h'))

vampire = bool({})

print(vampire)

#DECISION ( IF/ELIF/ ELSE)

# Buhari = 'Contest'

# if Buhari: 
#     print('JAPA')

# else:
#     print('JAPA STILL')


# Suzan_height = input('Input your height:  ')    

# if  float(Suzan_height) == 6.0:
#     print('You are Qualified')

# elif float(Suzan_height)  > 6.0:
#     print('Okay, you are good to go')

# else:
#   print('You are too short')

#change conditionals

# Aseoluwa = input ('Is Ase Contesting?: ')

# if Aseoluwa =='yes' or Aseoluwa =='YES':
#     print('Japa')

# else:
#     print('Stay in Nig')    


# age = input ('Input your age:')

# if int(age)==15:
#  print('You are eligible for the youth team')

# elif int(age) > 18:
#  print('Baba you are not 15')

# elif int(age) >15 :
#     print('Bro you are Older than 15')

# else:
#     print ('You are younger than 15') 




