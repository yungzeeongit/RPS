import random

def get_choices(): 
 player_choice =input("Enter a choice (rock,paper,scissors: ") 
 options = ["rock","paper","scissors"]
 computer_choice = random.choice(options)
 choices = {"player" : player_choice, "computer" : 
 computer_choice} 
 return choices


def check_win(player,computer):
  print(f"you choose {player}, computer chose {computer}.")
  if computer == player:
    return "it's a tie"
  elif player == "rock":
     if computer == "scissors":
       return "rock smashes scissors. You win!"
     else:
       return "paper covers rock. You lose"
  
  elif player == "paper":
     if computer == "rock":
       return "paper covers rock. You win!"
     else:
       return "scissors cuts paper. You lose"
       
  elif player == "scissors":
     if computer == "paper":
       return "scissors cuts paper. You win!"
     else:
       return "rock smashes scissors. You lose"


choices = get_choices()

result = check_win(choices["player"],choices["computer"])
print(choices)
print(result)



  
