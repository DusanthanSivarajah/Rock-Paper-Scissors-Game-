import random 


while True:

    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    User = None

    User = input("\nRock, Paper, or Scissors? ").lower()
    while User not in choices:
        User = input("Please select one of the following (Rock, Paper, or Scissors?))  ").lower()

    if User == computer:
        print("Computer: ", computer)
        print("User's Choice: ", User)
        print("Tie\n")
    elif User == "rock":
    
        if computer == "paper":
            print("Computer: ", computer)
            print("User's Choice: ", User)
            print("You Lose! :( \n")  
        if computer == "scissors":
            print("Computer: ", computer)
            print("User's Choice: ", User)
            print("You Win!! :) \n")
    elif User == "paper":
    
        if computer == "scissors":
            print("Computer: ", computer)
            print("User's Choice: ", User)
            print("You Lose! :( \n")  
        if computer == "rock":
            print("Computer: ", computer)
            print("User's Choice: ", User)
            print("You Win!! :) \n")
    
    elif User == "scissors":
    
        if computer == "rock":
            print("Computer: ", computer)
            print("User's Choice: ", User)
            print("You Lose! :( \n")  
        if computer == "paper":
            print("Computer: ", computer)
            print("User's Choice: ", User)
            print("You Win!! :) \n")
            
    play_again = input("Would you like to play again? Type Yes to play again: ").lower()
    
    if play_again != "yes":
        break
print ("hope you had fun! Have a nice day, bye! ")