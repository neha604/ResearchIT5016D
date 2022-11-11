#we are creating a game of rock paper and scissors
#between rock and paper,paper wins
#between paper & scissors ,scissors wins
#between scissors & rock, rock wins


#we will input random numbers from python functions, these are inbuilt




import random

winner=" "  #winner is placed in empty string

random_choice=random.randint(0,2)  #syntax of random


# since computer only understands binary we start with giving binary numbers against
# choices like 0=rock 1=paper and rest is scissors

if random_choice==0:
    computer_choice='rock'
elif random_choice==1:
    computer_choice='paper'
else:
    computer_choice='scissors'
    
user_choice=" "   #user choice is placed in empty string


#we are using while loop so computer keep asking for the input by user if by mistake
#user gives incorrect input like user writes "rack" in place of "rock"

while (user_choice!='rock'and user_choice!='paper' and user_choice!='scissors'):
    user_choice=input("rock,paper or scissors?")

#below conditions will tell who will win, we will write all conditions when
    #computer is winning
    
if computer_choice==user_choice:
    winner="tie"
elif computer_choice=='paper' and user_choice=='rock':
    winner='computer'
elif computer_choice=='rock' and user_choice=='scissors':
    winner='computer'
elif computer_choice=='scissors'and user_choice=='paper':
    winner='computer'
else:
    winner='user'

    
if winner=='tie':
    print("we both chose",computer_choice+"play again.")
    
else:
    print(winner,"won, i chose", computer_choice +'.')

#in last we write print statements which will tell who is the winner.

    

