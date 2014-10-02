#guess_num.py by rucury

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

"""
Dear person who is peer reviewing this code:
Check line 45 and remove the '#' symbol if you want.
This makes debugging or testing this code a lot easier.
It will show what the "secret number" is, so you can play
around with the code and enter the correct number when
you want to test the result of winning the game.

Thank you for reading. Good luck and have fun.
"""

import simplegui
import random

# initialize global variables used in your code
secretNum = 0
remainingGuesses = 0
currentRange = 100

# helper function to start and restart the game
def new_game(rangeOfNum):
    global secretNum, remainingGuesses, currentRange
    
    currentRange = rangeOfNum
    secretNum = random.randrange(rangeOfNum)
    
    if rangeOfNum == 100:
        remainingGuesses = 7
        
    elif rangeOfNum == 1000:
        remainingGuesses = 10
        
    else:
        "Error in changing remaining guesses!" # just in case
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "Guess the number!"
    print "The current range is 0 - " + str(rangeOfNum)
    print "You have " + str(remainingGuesses) + " guesses left!"
    #print "!!!!!! The secret num is", secretNum, "!!!!!!"
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "\n"

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    new_game(100)

def range1000():
    # button that changes range to range [0,1000) and restarts
    new_game(1000)
    
def input_guess(guess):
    # main game logic goes here	 
    
    global remainingGuesses, finishString
    
    if guess.isdigit():
        userGuess = int(guess)
        
        if userGuess != secretNum:
            finishString = 'ready'
            print "Your guess was " + guess + "!"
            remainingGuesses -= 1
   
        if userGuess == secretNum:
                print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                print "You guessed right! Well done!"
                print "The secret number was " + str(secretNum) + "."
                print ""
                print "Starting new game!"
                print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                print "\n"
                new_game(currentRange)
                return 0;
     
        elif remainingGuesses > 0: 
            print "You have " + str(remainingGuesses) + " guess(es) left!"
           
            if userGuess > secretNum:
                print "--- Guess lower! ---"
                print ""
                
            elif userGuess < secretNum:
                print "--- Guess higher! ---"
                print ""
                
        elif remainingGuesses == 0:
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            print "You ran out of guesses!!! Starting new game!"
            print "By the way, the secret number was " + str(secretNum) + "..."
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            print "\n"
            new_game(currentRange)
            return 0;
       
        else:
            print "Error in the input_guess function!" # just in case
            return 0;
    else:
        print "Numerical values only, please! Restarting game..."
        new_game(currentRange)
        return 0;
    
    return 0;
    
# create frame
f = simplegui.create_frame('Guess the number!', 100, 200)

# register event handlers for control elements
inp = f.add_input('Your guess:', input_guess, 50)
range100Button = f.add_button('Range: 0 - 100', range100)
range1000Button = f.add_button('Range: 0 - 1000', range1000)

# call new_game and start frame
new_game(currentRange)
f.start()
