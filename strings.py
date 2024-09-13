firstname = input("Hello, please enter your first name ")
lastname = input("Please enter your lastname ")

greeting = f"Hello, {firstname} {lastname}!"
print (greeting)
firstlength = len(firstname)
lastlenght = len(lastname)
longstr=len(firstname + lastname)
numberofcharacters = f"your name has, {longstr} characters"

print(f"your initials are {firstname[0]}{lastname[0]}")
doublename=""
for letter in firstname:
    doublename += letter +  letter
print(f"Double first name {doublename}")

print(f"backwards last name is {firstname[::-1]}")