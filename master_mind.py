print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('  Welcome in the compute programm')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
from random import randint
import time
import os

print('Do you want to train? [yes] or [no]')
game = input('Enter your answer : ')

while game != 'yes' and game != 'no':
    print('not possible answer, try again...')
    game = input()
print()

while game == 'yes':
    success = 0
    print('which operation do you want to train ? [-] or [+] or [*] ')
    choice = input('Enter your answer : ')
    print()
    
    if choice == '-':
        print('How many computes do you want to do?')
        times = int(input('Enter your answer : '))
        for i in range (0,times):             
            number = randint(2,100)
            number1 = randint(2,100)
            print('_______________________________\n')
            print('           ',number, '-',number1)
            print('_______________________________\n')            
            test = int(input('Enter your solution : '))
            print()
            if test == number - number1:
                print('\n             TRUE')
                success += 1
            else:
                print('\n            FALSE')
                
    elif choice == '*':
        print('A*B or A*BC or AB*CD? [0] or [1] or [2]')
        level = input('Enter your answer : ')
        while level != '0' and level != '1' and level != '2':
            print('bad value')
            level = input('Enter a new value : ')
        print('\nHow many computes do you want to do?')
        times = int(input('Enter your answer : '))
        for i in range (0,times):
            if level == '0':
                number = randint(2,9)
                number1 = randint(2,9)
            elif level == '1':
                number = randint(2,9)
                number1 = randint(2,99)
            elif level == '2':
                number = randint(2,99)
                number1 = randint(2,99)  
            print('_______________________________\n')
            print('           ',number, '*',number1)
            print('_______________________________\n')            
            test = int(input('Enter your solution : '))
            if test == number * number1:
                print('\n             TRUE')
                success += 1
            else:
                print('\n            FALSE')                
    elif choice == '+':
        print('How many computes do you want to do?')
        times = int(input('Enter your answer : '))
        for i in range (0,times):             
            number = randint(2,100)
            number1 = randint(2,100)
            print('_______________________________\n')
            print('           ',number, '+',number1)
            print('_______________________________\n')
            test = int(input('Enter your solution : '))
            if test == number + number1:
                print('\n             TRUE')
                success += 1
            else:
                print('\n            FALSE')
    else:
        print('bad input')
    print('===============================')    
    print('\nYou get ', success,'/',times, ', retry? [yes] or [no]')
    game = input('Enter your answer : ')

os.system('Pause')
