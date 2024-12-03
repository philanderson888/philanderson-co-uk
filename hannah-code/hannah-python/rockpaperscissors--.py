import random

Choices = ['rock', 'paper', 'scissors']

users_choice = input("What is your name?")
x = {users_choice}

print("We are going to start playing now.")
user_choice = input("Rock, Paper, or Scissors? ")

if user_choice in Choices:
        computer_choice = random.choice(Choices)
        print("You chose: ", user_choice)
        print("Bot chose: ", computer_choice)
else:
        print("You put '{user_choice}' which means you didnt choose a valid response.")

        
if user_choice == computer_choice:
    print("This means.. It's a tie!")

elif user_choice == 'rock' and computer_choice == 'scissors':
    print("This means.. You've won. (But only this round haha)")

elif user_choice == 'scissors' and computer_choice == 'paper':
    print("This means.. You've won. (But only this round haha)")

elif user_choice == 'paper' and computer_choice == 'rock':
    print("This means.. You've won.")

else:
    print("This means.. You've lost! Oh No!")
    print("Computer said 'Do Better Next Time.'")








