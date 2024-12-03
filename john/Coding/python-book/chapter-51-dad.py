people = ["mum","dad","philip"]

quit = False 
match = False

while (not quit):

    # get user choice

    user_choice = input("enter a person ")
    print(f"you chose {user_choice}")
    if user_choice == "q":
        print('quitting match')
        quit = True
        break


    # compare user choice with valid answers
    for person in people:
        if person == user_choice:
            print(f'we got a match!!! on {user_choice}')
            match = True
            break

    
    # is there a match?
    if match:
        print(f'there is a match')
    else:
        print('no match')