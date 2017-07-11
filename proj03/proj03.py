# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
x=raw_input('Guess any number between 1 and 9: ')
x=int(x)
import random
variable_name=random.randint(1,9)
while variable_name != x:
    if x<variable_name:
        print ('that number is too small!')
        x=raw_input('guess again')
        x=int(x)
    if x > variable_name:
        print('that number is too big!')
        x=raw_input('guess again')
        x=int(x)
    if x == variable_name:
        print ('you guessed the number!')





