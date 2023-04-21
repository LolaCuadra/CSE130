# 1. Name: 
#    Dolores Cuadra
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    we had to do a random number guesser in order for us to review the basics from python. we basically just had to set a  number for the game dfficulty, and the player had to guessed it.
# 4. What was the hardest part? Be as specific as possible.
# not going to lie, I had to check w3Schools to check to do an user input zdn what was the sentinal for
# 5. How long did it take for you to complete the assignment?
#   about an hour and a half, but if we count the time me reading stuff on how to the simpliest stuff like why is it True and not "true" or "TRUE," I'll say 2 hours and a half 

import random

# Game introduction.
print("this is a guessing game!")
# Prompt the user for how difficult the game will be. Ask for an integer.
max_guess = int(input("How high do you want the number range to be? "))
# Generate a random number between 1 and the chosen value.
value_random = random.randint(1, max_guess)

# Give the user instructions as to what he or she will be doing.
print(f"Im guessing on a number between 1 and {max_guess} guess what it is!")
# Initialize the sentinal and the array of guesses.
sentinal = False
guesses = []

# Play the guessing game.
while not sentinal:
    # Prompt the user for a number.
    guess = int(input("guess a number?"))

    # Store the number in an array so it can be displayed later.
    guesses.append(guess)
    # Make a decision: was the guess too high, too low, or just right.
    if guess < value_random:
        print("too low!")
    elif guess >  value_random:
        print("too high!")
    else:
        print("perfect! you did it!")
        sentinal = True

# Give the user a report: How many guesses and what the guesses where.
print("you guess the number in", len(guesses),"tries. your guesses were:", guesses)