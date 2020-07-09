#an unwinnable Rock_Scissors_Paper Game
print("This is game actually checks both player inputs.")
player_choice = input("Enter r for Rock, s for Scissors and p for Paper (r/s/p): ")

#Reminder: lists start counting from 0. so list[0] is the first item
#choices[0] is rock, choices[1] is scissors, choices[2] is paper
choices = ["rock","scissors","paper"]




if player_choice == "r":
    opponent_choice = choices[2]
if player_choice == "s":
    opponent_choice = choices[0]
if player_choice == "p":
    opponent_choice = choices[1]
print("Opponent chose", opponent_choice)
## Check both choices
if player_choice == "r":
    if opponent_choice == "paper":
        print("Opponent wins!")
    elif opponent_choice == "scissors":
        print("You win!")
    else:
        print("Try again.")
if player_choice == "s":
    if opponent_choice == "rock":
        print("Opponent wins!")
    elif opponent_choice == "paper":
        print("You win!")
    else:
        print("Try again.")
if player_choice == "p":
    if opponent_choice == "scissors":
        print("Opponent wins!")
    elif opponent_choice == "rock":
        print("You win!")
    else:
        print("Try again.")

        
        
