import random

gameover = False # flag

while gameover == False:
  ai_choice = random.randint(0,2)
  a = int(input("scissors(0) paper(1) or stone(2):"))
  if a == 0 and ai_choice== 0:
    print("AI chooses scissors")
    print("Tie")
  if a == 0 and  ai_choice== 1:
    print("AI chooses paper")
    print("You Win")
  if a == 0 and ai_choice== 2:
    print("AI chooses stone")
    print("You Lose")
  if a == 1 and ai_choice== 0:
    print("AI chooses scissors")
    print("You Lose")
  if a == 2 and ai_choice== 0:
    print("AI chooses scissors")
    print("You Win")
  if a == 1 and ai_choice== 1:
    print("AI chooses paper")
    print("Tie")
  if a == 2 and ai_choice== 2:
    print("AI chooses stone")
    print("Tie")

  if a == 2 and ai_choice== 1:
    print("AI chooses paper")
    print("you lose")
    
  if a == 1 and ai_choice== 2:
    print("AI chooses stone")
    print("you win")
  # end of scissors paper stone
  yes_or_no = input("DO you want to continue(y/n)")
  if yes_or_no == "n":
    gameover = True
