import random
random.randint(1,10)


randintg = random.randint(1,10)
print(randintg)
print("enter ´000´ TO STOP THE GAME")

print("Guess the number between 1 and 10")
guess = input("Choose a number ")
guess = int(guess)
if guess == randintg:
    print("congratulations, you won")
while guess != randintg:
    if guess == 000:
        print("you closed the game")
        break
    if guess < randintg:
        print("too low try again")
        print("please enter another value")
        guess = int(input(" "))
    elif guess > randintg:
        print("too high try again")
        print("please enter another value")
        guess = int(input(" "))
if guess == randintg:
    print("congratulations, you won")