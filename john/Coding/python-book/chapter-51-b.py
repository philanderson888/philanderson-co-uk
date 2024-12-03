date = "Tuesday 30/08/22"
print(date)

# Create array
nice_chocolates = ["Wispa", "Maltesers", "Twix", "Galaxy"]

# Create loop and get user input
user_input = ""
quit = False
while user_input != "q":
    input("Type a chocolate, or q to stop: ")
    if user_input != "q":
        match_found = False

        # does user input match array
        print(nice_chocolates)
        print(user_input)
        print(match_found)

        for a_chocalate in nice_chocolates:
            if user_input == nice_chocolates:
                match_found = True
                break

# print output
            if match_found == True:
                print("This is on our list of nice chocolates.")
            else:
                print("This is not a nice chocolate..")