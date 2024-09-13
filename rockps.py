import random
print("lets play a game")
options = ["Rock","Paper","Scissors"]




while True:
    user_ch = input("Chose: Rock, Paper, Scisors:")
    compch = random.choice(options)
    print (f"Computer choise is {compch}")
    if user_ch == "Quit":
        print(f"Goodbye my guess whould have been {compch}")
        break
    if user_ch == compch:
        print("tie, try again")
    elif (user_ch == "Rock" and compch == "Scissors") or (user_ch == "Paper" and compch == "Rock") or (user_ch == "Scissors" and compch == "Paper"):
        print("User won")
    else:
        print("computer won")