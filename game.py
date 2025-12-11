import random

print("Welcome to rock-paper-scissors!")

choice = str(input("Choose rock, paper, or scissors: "))

print("You chose:" , choice)

poss = ["rock", "paper", "scissors"]
choice = random.choice(poss)
print(f"computer chose {choice}.")