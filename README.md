import random

secret_number=random.randint(1,100) # Generate the random number between 1 to 100

attempet=0
Max_attempet=10

while attempet<Max_attempet:
    guess=int(input('Enter the Guess number :'))
    attempet +=1

    if guess==secret_number:
        print('Congratulations! Ypour guessed number is correced.')
        print('attempet used', attempet)
        break
    elif guess>secret_number:
        print('Too high!')
    else:
        print('Too Low!')
    
    print('Attempet Left :',Max_attempet-attempet)

    #Game Over Condition
    if attempet==Max_attempet and guess!=secret_number:
        print('Game Over!')
        print('The correct number was :',secret_number)
        
