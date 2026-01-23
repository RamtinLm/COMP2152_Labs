import random

# Soloution for the Week 02 Lab 02
# Ramtin Loghmani

choices = ["Rock", "Paper", "Scissors"]
# print(choices)

playerChoice = input ("Enter a number between 1 to 3 for the following chioces: \n1. Rock \n2. Paper \n3. Scissors\n")

playerChoice = int(playerChoice)
if playerChoice < 1 or playerChoice > 3:
    print("Error: Please select a number between 1 and 3.")
else:
    # Develop the game logic using if/elif/else
    # random is a package that helps us generate random numbers. it is built in to python.
    computerChoice = random.randint(1, 3)

    if playerChoice == computerChoice:
        print("It's a tie! Both selected", choices[playerChoice - 1])
    elif (playerChoice == 1 and computerChoice == 3) or \
         (playerChoice == 2 and computerChoice == 1) or \
         (playerChoice == 3 and computerChoice == 2):
        print("You win! You selected", choices[playerChoice - 1], "and the computer selected", choices[computerChoice - 1])
    else:
        print("You lose! You selected", choices[playerChoice - 1], "and the computer selected", choices[computerChoice - 1])