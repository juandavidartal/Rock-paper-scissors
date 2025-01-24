import random
import time

#List with Rock, Paper, Scissors
rps = ["Rock", "Paper", "Scissors"] 

#Initialize Counters
player_counter = 0
computer_counter = 0

#Rock, Paper, Scissors function
def game(player_counter, computer_counter):
    #Player chooses Rock
    if player_choice == 0:
        if computer_choice == 0:
            print("It's a draw!")
        
        elif computer_choice == 1:
            print("Computer wins!")
            computer_counter += 1
        else:
            print("You win!")
            player_counter += 1
    #Player chooses Paper
    elif player_choice == 1:
        if computer_choice == 1:
            print("It's a draw!")
        
        elif computer_choice == 2:
            print("Computer wins!")
            computer_counter += 1
        else:
            print("You win!")
            player_counter += 1
    #Player chooses Scissors
    elif player_choice == 2:
        if computer_choice == 2:
            print("It's a draw!")
        
        elif computer_choice == 0:
            print("Computer wins!")
            computer_counter += 1
        else:
            print("You win!")
            player_counter += 1
    return player_counter, computer_counter

#Greetings
print("Welcome to Rock, Paper & Scissors!\n\n")

#Ask Username
username  = str(input("What's your name, contender?\n"))

print(f"Hi,{username}! Get ready for some fun!\n")

#Executes a loop with the game
while True:

    #Ask for text input, evaluate if it's a correct input
    player_input = str(input("Pick your weapon: Rock, Paper or Scissors \n\n").capitalize())

    try:
        player_choice = rps.index(player_input)
    except ValueError:
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")
        continue
    #Countdown    
    print("\n3\n")
    time.sleep(1)
    print("2\n")
    time.sleep(1)
    print("1\n")
    time.sleep(1)


    computer_choice = random.randint(0, 2)
    print("Computer picked:", rps[computer_choice], "\n\n")
    time.sleep(1)

    # Call the game function and update the counters
    player_counter, computer_counter = game(player_counter, computer_counter)

    time.sleep(1)
    print("\n")
    print(f"{username}: {player_counter}")
    print(f"Computer: {computer_counter}")
    print("\n\nLet's play again! \n\n")
