import random


CHOICES = ['rock', 'paper', 'scissors']

print("What is your name?")
users_choice = input(" Type your name: ")
y = {users_choice}

while True:
    print('Make your throw.')
    user_choice = input(" Type rock, paper, or scissors: ")
    if user_choice in CHOICES:
        computer_choice = random.choice(CHOICES)
        print(
            f"\nYou threw '{user_choice}', your component threw '{computer_choice}'"
        )
    else:
        print(
            f"\nYou typed '{user_choice}' which isn't a valid throw"
        )
    again = input(f"\nWant To Play More {users_choice}?")
    if again.lower() == "n":
        break
    print("\nGoodbye")

