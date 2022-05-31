#FUCTIONS
#DEFINITION  FUCTIONNAME (PARAMETER)
# RETURN STATEMENT

def addTwo(x):

    return x + 2

newNumber = addTwo(4)
print(newNumber)
    # OR
print(addTwo(4))

# for i in range(0,10,2):
#     def show():
#         print(i * 2)
#     show()    

def SubTwo(y):

    return y - 2

newNumber = SubTwo(4)
print(newNumber) 
#    OR
print(SubTwo(4))   


def printString(str):

        return (str)

printsungbalaja = printString('Mariam sungabalaja')
print(printsungbalaja)


def force (mass, acceleration):
    return (mass * acceleration)
        #  OR
      # f = mass * acceleration
    # return f    

p = force(3,9)   
print(p) 

print(force(3,9))


# SOMETIMES YOU DON'T NEED A PARAMENTER

def doSomething():
    print('Hi')

doSomething()    

# OPTIONAL PARAMETERS (Using multiple parameters)

def multi (x, text):
    print(x , text)
    # if text == 'Omome':
    #     print('Ase')
    # else:
    #     print('Name not found')    

multi ('Owah','')    
multi ('Owah','Omome')    

#if you do not want to constantly write parameters(()),
#we can give a default value for parameters, like a dealt value of x.
#Then if we want text to be set to something we can do:
#def func(x, text= '4')

def multi (x, text='4'):
    print(text)
    if text == '1':
        print('Text is 1')
    else:
        print('Text is not 1')    

multi ('Ore','4')    
multi ('Ore','20')


  

