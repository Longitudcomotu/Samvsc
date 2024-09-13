import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
        print("Do you want to know the other ending? (yes or no)")
        option=input(str())
        if option =="yes" or option == "y":
            print('Gobbles you down in one bite! you are so bad bro')

    
               
    else:
        print('Gobbles you down in one bite! you are so bad bro')
        print("Do you want to know the other ending? (yes or no)")
        option=input(str())
        if option == "yes" or option == "y":
            print('Gives you his treasure!')
        
        
    
    

playAgain = 'yes'
while playAgain.lower() in ['yes', 'y']:
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
    
    
