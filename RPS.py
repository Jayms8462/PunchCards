import random

play = input("Lets play Rock, Paper, Scissors, do you want to play? Y/N: ")

def sg():
    systemGuess = random.randint(1,3)
    if systemGuess == 1:
        systemGuess = "R"
    elif systemGuess == 2:
        systemGuess = "P"
    elif systemGuess == 3:
        systemGuess = "S"
    return systemGuess
    
while play != "N":
    guess = input("Press R for Rock, P for Paper, S for Scissors.")
    print("\nYour Guess: " + guess)
    print("\nComputers Guess: " + sg())
    print("\n")

    if guess == "R" and sg() == "S":
        print("You Win")
        play = input("Play Again? Y/N: ")
    elif guess == "P" and sg() == "R":
        print("You Win")
        play = input("Play Again? Y/N: ")
    elif guess == "S" and sg() == "P":
        print("You Win")
        play = input("Play Again? Y/N: ")
    elif guess == sg():
        print("You Tied")
        play = input("Play Again? Y/N: ")
    else:
        print("You Lost")
        play = input("Play Again? Y/N: ")

print("So long and thx for all the fish.")