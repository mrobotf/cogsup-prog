"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""

import random

print("Think of a number between 1 and 100 (inclusive) and I will try to guess it.")
input("Press Enter when you're ready...")

# Set the initial range for guessing
low = 1
high = 100

# Initialize feedback variable
feedback = ''

# Continue until the computer guesses correctly
while feedback != 'c':
    
    # Computer makes a guess within the current range
    guess = random.randint(low, high)
    
    # Get user feedback
    feedback = input(f"My guess is {guess}. Is it too high (H), too low (L), or correct (C)? ").lower()
    
    # If the guess is too high
    if feedback == 'h':
        
        # Adjust the upper bound of the range
        high = guess-1

    # If the guess is too low
    elif feedback == 'l':

        # Adjust the lower bound of the range
        low = guess+1
    
    # If the input is invalid
    elif feedback != 'c':
        
        # Prompt for valid input
        print("Please respond with 'H', 'L', or 'C'.")