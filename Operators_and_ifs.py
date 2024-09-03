Guess = input("Give me a number between 1 and 10: ")
Guess = int(Guess)
if Guess <3:
    print("You guessed too low")
elif Guess == 3:
    print("You are correct")
elif Guess > 10:
    print("That is not a valid number")
else:
    print("You guessed too high")