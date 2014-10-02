#rpslp.py by rucury

import random

# helper functions

def number_to_name(number):
    
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        #just in case
        return 'Error in the number_to_name function!'

    
def name_to_number(name):
    
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        #just in case
        return 'Error in the name_to_number function!'


def rpsls(name): 
    
    player_number = name_to_number(name)
    comp_number = random.randrange(5)
    
    difference = (player_number - comp_number) % 5
    

    print "Player chooses " + number_to_name(player_number)
    
    print "Computer chooses " + number_to_name(comp_number)
    
    if difference == 1 or difference == 2:
        print "Player wins!"
    elif difference == 3 or difference == 4:
        print "Computer wins!"
    else:
        print "Player and computer tie!"
        
    print "" #blank line between games
    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



