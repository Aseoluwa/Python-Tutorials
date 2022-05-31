# from random import randint

# number = randint (1,5)

# player_name = input('Hi, What is your name?:\n')

# print('Okay!',player_name,'I am guessing a number btw 1 and 10' )

# number_of_guesses =0
# while number_of_guesses < 5:
#     guess = int(input('Guess a number:'))
#     print(guess)
#     number_of_guesses = number_of_guesses + 1

#     if guess == number:
#         print(player_name,'You guesseed correctly')

#         break

#     elif guess > number:
#         print('You guessed too high')
#     elif guess < number:
#         print('You guess is too low')    

   


# if guess == number:
#         print('You guessed the number in ' + str( number_of_guesses) + ' tries!!')  

# else:
#     print('You did not guess right, the answer is', number)      



# class Dog(object)

# from random import randint


class Female(object):
    def __init__(self,name,language, skin, skill):
        self.name = name
        self.language = language 
        self.skin = skin
        self.skill = skill
        print('Nice you made a female')
        # pass
    def speak(self):
        print('My name is', self.name, 'i am', self.skin, 'in complexion')
        # pass
    def lang(self):
        print('I speak', self.language, 'and i am', self.skin, 'skinned')

    def hobby(self):
        print('I love', self.skill)   

class Male(Female):
    def __init__(self, name, language, skin, skill, age):
        super(). __init__(name, language, skin, skill)
        self.age = age
        print('You have a male')

    def speak(self):
        print('Hi, my name is', self.name, 'I am an intro tech teacher and i am ', self.age, 'years old')  

class Mum (Male):
    def __init__(self,name,language, skin, skill,age, month):
        super(). __init__(name, language, skin, skill,age)
        self.month= month     
        print('you were born i August')

    def speak(self):
        print('Hi', self.name, 'was born in the month of ', self.month)        

        
steph = Female('Stephanie', 'Hausa', 'fair', 'Playing')
tosin = Female('Tosin', 'YORUBA', 'caramel', 'Singing')
mariam = Female('Maria', 'IGBO', 'dark', 'Running')
steph.speak()
tosin.speak()
mariam.speak()
tosin.lang()
steph.hobby()
tosin.hobby()
mariam.hobby()
Prof = Male('Sege', 'Hausa', 'fair', 'coding', 2)
Prof.speak()
moni= Mum('Sege', 'Hausa', 'fair', 'coding',2, 'September')
moni.speak()