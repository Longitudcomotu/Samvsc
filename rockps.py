#Rock paper scissors game



import random
def result(text):
    print(f"**********{text}**********")
options = ["1","2","3"]
computer_options=["rock","paper","scissors"]
while True:
    user_ch = input("Choose rock(1), paper(2), scissors(3): ")
    computer_ch = random.choice(computer_options)
    print(computer_ch)
    if user_ch == "quit":
        result("goodbye")
        break
    if user_ch not in options:
        result("not allowed, please enter a valid option")
        continue
    if user_ch=="1":
        user_ch="rock"
    elif user_ch=="2":
        user_ch="paper"
    elif user_ch=="3":
        user_ch="scissors"
 
   
    print(user_ch)
    if user_ch == computer_ch:
        result("its a tie, try again")

   
    elif ((user_ch == "rock") and computer_ch == "scissors") or ((user_ch == "paper") and (computer_ch == "rock")) or ((user_ch == "scissors") and (computer_ch == "paper")):
        result("You win, congratulations")
    
    else:
        result("You lose bro")
        
        
