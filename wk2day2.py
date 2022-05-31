# INTRODUCTION TO MODULAR PROGRAMMING
# # Python is modular programming language meaningyou can use many modules to create one programme(using import statements).
# # There are many built-in modules in python that contain a list of functions and classes we can use in python script  e.g math

# # import math(allows us to do something like sqrt()) - also notice the color of the import text, meaning keyword
# # import pygame(game development with python)
# # import os(gives bus the opportunity to do file paths i.e import images e.t.c into our files in python)

# # MATH MODULE (import math)- This is a built in model downloaded when python is installed. 
# # N.B Python is an open source language, meaning you can actually create your own modules
# # and they contain functions, classes that can be used in different programmes or can be sent to friends/posted

# # To use the math module


import math

import inspect
import myModule

# import queue from  queue
# import rv.rvtypes


#math.name of the fuction or class
print(math.pi)
print(math.degrees(30))
print(math.radians(1718.873))
print(math.degrees(math.pi))

def func(x):
    if x == 1:
        def rv():
            print('X is equal to 1')

    else:
        def rv():
            print('X is not equals to 1')        

    return rv

newFunc = func(1) 
newFunc()


#to get momory address
print(id(newFunc))   

#print(inspect.getmembers(newFunc)) #you have to import inspect modul line 6
# print(inspect.getsource(newFunc))  #you have to import inspect module in line 6
#print(inspect.getsource(Queue)) ##f"rom queue import Queue" line 6 (shows codes used in creating object OR Classes)

# print(inspect.getmembers(newFunc))  
# print(inspect.getsource(newFunc))      

#other more complicated example of optional parameters depending on inheritance

#CLASSES AND OBJECTS(iNTRODUCING OBJECTS)
##An object :in py, an object is [pretty much anything built into a class and has an instance of a variable . eg  RUN this]


x = 3
y = 'strings'

print(type(x))
print(type(y))

print(type(x-8))

import turtle
x = 4
y = 'string'


rhema = turtle.Turtle()
#how to import a module into out function (import myModule)
# step 1: create  a new file in this directory called myModule.py

Ase = myModule.myFunc(2)
print(Ase)
    #  OR

# print(myModule.myFunc(3)) 
# 
# Ola= myModule.newone(31)
# print(Ola)


#for the method: It is anything you call on an object 
# It is what you call with a dot operator(.)
# eg'Turtle()' is a methid that creats a new turtle object

x = 5

y = 'meet'

print(y.upper())
print(y.replace('e','b'))

#CLASSESS AND OBJECTS 2

#TO REGISTER INSTANCES IN CLASSES
#STEP1: IN YOUR def __Init, state the parameter(self, name) EG: def __init__(self, name):
#STEP2: REGISTER THE PARAMETER OR QUALIFY THE PARAMETER EG:(SELF.NAME =NAME)
#STEP3: USE THE QUALIFIED PARAMETER WITHIN ANOTHER METHOD EG: ,self.name
#STEP4: INPUT THE ARGUMENT WHICH IS VALUE FOR THE PARAMETER(roman)
#STEP5: CALL THE METHOD THE METHOD ON THE OBJECT THAT HAS THE ARGUMEN EG: roman.speak()

class Dog():
    def __init__(self, name,age):
        self.name = name
        self.age = age
        print('Nice you made a dog')
        # pass

    def speak(self):
        print('Hi, I am',self.name)

        #  pass

    def all(self):
        print('Hi i am ,', self.name, ',and i am ',self.age, ',years old')    

roman = Dog('Roman', 24)  
henry = Dog('Henry', 2)  
roman.speak()  
henry.all()
roman.all()
                
                  #   OR

class All():
    def __init__(self, name, age):
        self.name= name
        self.age = age
        print('Nice to meet you')
        # pass

    def sentenc2 (self):
        print('Hi',self.name,)

    def lasts (self):
        print(self.name, 'is only admite', self.age, 'years to this program')    


Bola = All('Bolanle',2)
Usman = All('Mohamed',3)
Bola.sentenc2()
Usman.lasts()



