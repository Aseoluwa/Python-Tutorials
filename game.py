from random import randint

Option = ['Rock','Paper','Scissors']
Computer = Option[randint(0,2)]

print(Computer)

player = False

while player == False:
    player = input ('Rock,Paper,Scissors: ')
    player = player.lower()
    player = player.capitalize()
    print(player)
    if player == Computer:
     print('Tie')

    elif player  == 'Rock':
        if Computer =='Paper':
            print('You lose',Computer, 'Cover', player)
        else:
            print('You win π', Computer, 'loss')    
    elif player == 'Paper':
        if Computer == 'Rock':
            print ('You win π',player,'Covers' ,Computer)
        else:    
            print('You loss',Computer, 'Wins!π')

    elif player == 'Scissors':
        if Computer == 'Paper':
            print('You win π', player, 'covers' ,Computer)   
        else:
            print('You Loss', Computer, 'Winsπ') 
# else:
#     print("Thats not a valid play, Check your spelling!")
    
    player = False
    computer =  Option[randint(0,2)]      

