# x = 4
# print(x)
# y= 55

# print (type(y))
# con =float(y)
# print(con)
# con =bool(x)
# print(con)


# name = 'Rhema'
# age='20'
# networth= '27bn'
# print('Hey my name is', name, 'and i am', age, 'my networth is', networth)

# num1 = '3'
# num2 ='6'
# print(num1 + num2)
# num3 =int(num1)
# num4= int(num2)
# print(num3 + num4)

# SUM = int(num2) - int(num1)
# print(SUM)

# print ('Pick a number')
# numb = input()
# print ('You are', numb, 'years of age')


# Job_offer = input('Input your years of experience =')

# if int(Job_offer) == 5 :
#     print('You are Qualifed for the Job')

# elif int(Job_offer) <=4 :
#     print('You have one more stage to qualify for the job')

# else:
#     print('This job is not meant for you. Try again next year')  


# Password =input('Input your password')

# if 

# username = 'Faith'

# password = 'Faith123'
 
# User_input = input('What is your name?\n')

# if User_input == username:
#     Login= input('Password:\n')
#     if Login ==password:
#         print('You have login succesfuly')
#     else:
#         print('Username or Password wrongly inputted😞')

# else:
#     print('Username or Password wrongly inputted😞')



# from re import X


# file = open('aaaa.txt','r' ) 
# f = file.readlines()
# print(f)   

# newlist =[]
# for line in f:
#     if line [-1] =='\n':
#         newlist.append(line[:-1])

#     else:
#         newlist.append(line)
# print(newlist)  

# newList =[]
# for line in f:
#     newList.append(line[:-1])  

# print(newList)       

# newList = []
# for line in f:
#     newList.append(line.strip())

# print(newList)    

# Bola = 72
# Funke= 44

# if Funke >Bola:
#     print('Funke is greater')


# else: 
#      print('Na Bola Old oh')

# else:
#     print('Oyo oh')    

# file = open('aaaa.txt', 'w')
# write = file.write('Bola\nis\na\nBoy')
# print(write)

# file =open('aaaa.txt', 'w')

# file.write('Oga\nAde\nand \nTunde\nare\ncrinimals')
# file.close()

# x =2
# y = 3

# if x == y and x + y ==5:
#     print('And is Okay')

# if x == y or  x + y ==5:
#     print('OR Worked')
#     if y==x and x==y:
#         print('And 2 worked')



# list1 = ['apple', 'samsung','redmi','infinix', 'tecno','redmi']
# print(list1)

# for y in range (0, 10,2):
#     print (y)

# for x in range (0,11):
#     print(x)

# trp_1 = ('apple', 'samsung', 'redmi', 'infinix', 'redmi', 'tecno')    

# convert =list (trp_1)
# print(convert)
# convert.remove('samsung')
# print(convert)

# Math =input ('Input your Maths score\n')
# English = input('Input Your English Score\n')
# Physics = input ('Input your Physics score\n')
# Chemistry = input('Input your Chemistry score\n')

# Sub = ['Math','English','Physics','Chemistry']
# Score = [Math,English,Physics,Chemistry]

# print('')

# for x in range (0,len(Score)):
#     if (Score[x].isdigit()):
#         if (int(Score[x]) >=80):
#             print('Your',{Sub[x]},'Score is  A')
#         elif (int(Score[x])>=60):
#                 print('Your',{Sub[x]},'Score is  B')
#         elif (int(Score[x]) >=40):
#                 print ('Your',{Sub[x]}, 'Score is  C')
#         elif (int(Score[x]) >0) :
#             print('Your',{Sub[x]}, 'Score is  F \n Sorry you Failed')  
# else:
#     print('ABOVE IS YOUR EXAM RESULT😊')



     


# if int([Math,English,Physics,Chemistry]) >= 80 :
#     print ('A')
#     if int([Math,English,Physics,Chemistry]) >60:
#      print('B')
#      if int([Math,English,Physics,Chemistry]) >50:
#       print ('C')
#       if [Math,English,Physics,Chemistry] > 45:
#           print('D')
        
# else:
#     print('You failed')     
   
import random
import array

Maxpasslen = 12

Num =['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

Lcase =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

Ucase= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K']

Sym = ['@', '#', '$', '%', '=', ':', '?']

Ran_Num = random.choice(Num)
Ran_lcase =random.choice(Lcase)
Ran_Ucase = random.choice(Ucase)
Ran_Sym= random.choice(Sym)

password = Ran_Num + Ran_Ucase + Ran_lcase + Ran_Ucase + Ran_lcase +Ran_Sym +Ran_Sym
    
print(password)

# import re
# re.compile('<title>(.*)</title>')



# password = input ('input your password!: ')

# while True:

#  is_valid = 0

#  if (len(password)<5):
#     print("Password should have at least 6 characters") 
#  elif (len(password)>12):
#     print("Password should not exceed least 12  characters") 
#  elif not re.search("[A-Z]", password):
#     print("Invalid! Password should contain at least one alphabet in Uppercase")
#  elif not re.search("[a-z]", password):
#     print("Invalid! Password should contain at least one alpahbet in lowercase") 
#  elif not re.search("[0-9]", password):
#     print("Invalid! Password should coantain at least one number")
    
#  else:
    
#   is_valid = 1
#   print("Valid password")