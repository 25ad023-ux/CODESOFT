import random

user = input("Enter rock, paper or scissors: ")
computer = random.choice(["rock", "paper", "scissors"])

print("You:", user)
print("Computer:", computer)

if user == computer:
    print("Tie")
elif (user == "rock" and computer == "scissors") or \
     (user == "scissors" and computer == "paper") or \
     (user == "paper" and computer == "rock"):
    print("You win")
else:
    print("You lose")
