import random

# IS 650
# Melanie Brown
# Rock, Paper, Scissors Game

choice: list = ["rock", "paper", "scissors"]

userChoice: str = input("Choose rock, paper, or scissors and type your answer: ")

while True:
  userChoice: str = (input("Choose rock, paper, or scissors and type your answer: "))
  if userChoice in choice:
    break
  print("Invalid choice. Please choose between rock, paper, or scissors.")

computerChoice = random.choice(choice)
print("The computer chose: ", computerChoice)

if userChoice == computerChoice:
  print("It's a tie.")
elif userChoice == "rock" and computerChoice == "scissors":
  print("You win!")
elif userChoice == "paper" and computerChoice == "rock":
  print("You win!")
elif userChoice == "scissors" and computerChoice == "paper":
  print("You win!")
elif userChoice == "rock" and computerChoice == "paper":
  print("The computer wins!")
elif userChoice == "paper" and computerChoice == "scissors":
  print("The computer wins!")
elif userChoice == "scissors" and computerChoice == "rock":
  print("The computer wins!")