import random

Choices = ["rock", "paper", "scissors"]

user_input = input("Type rock for rock, paper for paper, scissors for scissors: ")

ComputerWins = 0
PlayerWins = 0

if user_input in Choices:
    computer_input = random.choice(Choices)
    print("You have picked " + user_input)
    print("Computer has  picked " + computer_input)
else:
    print(user_input + "is not a correct choice, play again")

if user_input == "rock":
    if computer_input == "rock":
        print("It's a tie!")
        # repeat
    if computer_input == "paper":
        ComputerWins += 1
        print("Computer Wins")
    if computer_input == "scissors":
        PlayerWins += 1
        print("You Win!")

if user_input == "paper":
    if computer_input == "rock":
        PlayerWins =+ 1
        print("You Win!")
        # repeat
    if computer_input == "paper":
        print("It's a tie!")
    if computer_input == "scissors":
        ComputerWins += 1
        print("Computer Wins")

if user_input == "scissors":
    if computer_input == "rock":
        ComputerWins =+ 1
        print("Computer Wins")
        # repeat
    if computer_input == "paper":
        PlayerWins += 1
        print("You Win!")
    if computer_input == "scissors":
        print("It's a tie!")

