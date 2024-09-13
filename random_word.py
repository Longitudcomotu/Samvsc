
print("Guess the word")
import random

print("List of words to choose from:")

word_list = ["python","java","javascript","ruby","html","css"]
print(word_list)
# Randomly select a word from the list
selected_word = random.choice(word_list)
# Initialize the user's guess
user_guess = input("Enter your guess: ")
while user_guess != selected_word:
    user_guess = input("try again: ")
    if user_guess == selected_word:
        print("you won bro, see ya")
        break
    