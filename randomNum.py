#main.py
import random

n = random.randint(1,20)

guess = int(input("Guess a number between 1 and 20 or select a number greater than 20 to exit: "))

while guess != n:
    if guess > 20:
        print("Sorry to see you go.")
        break
    if guess < n:
        guess = int(input("Guess a higher number, or select a number greater than 20 to exit: "))
    elif guess > n:
        guess = int(input("Guess a lower number, or select a number greater than 20 to exit: "))

if guess == n:
    print("congratz your guess: ")
    print(guess)
    print("was the correct number.")