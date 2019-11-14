#WHILE LOOPS
'''
i=1
while i<=10:
    print('*'*i)
    i+=1
print ('Done')
'''

#GUESSING GAME
'''secret_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input('Guess: '))
    guess_count+=1
    if guess == secret_number:
        print('You won!!!')
        break
else:
    print('Sorry You lost :-(')
'''

#CAR SIMULATION GAME
'''default_input='HELP'
user_input=input('>')
while user_input.upper() == default_input:
    print('start - to start  the car')
    print('stop - to stop  the car')
    print('quit - to quit')
if user_input == 'start':
    print ('Car started . . .  Ready to Go...!')
elif user_input == 'stop':
    print('Car Stopped')
'''
#Solution
'''command=''
Started = False
while True:
    command=input('>').lower()
    if command == 'start':
        if Started == True:
            print('Car is already started !!! Dont spoil the Engine')
        else:
            Started=True
            print('The car has been started . . .')
    elif command == 'stop':
        if not Started:
            print ('Hey the Car is already stopped')
        else:
            Started =False
            print('car has been stopped !!')
    elif command == 'help':
        print('''
'''Start - To start the car
Stop - To stop the car
Quit - to quit the game'''
''')
    elif command == 'quit':
        break
    else:
        print("I Don't Unserstand that")
'''









