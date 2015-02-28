# Rock-paper-scissors-lizard-Spock game

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

def name_to_number(name):     # Converts name to number 
    if name == "rock":
        name = 0
    elif name == "Spock":
        name = 1
    elif name == "paper":
        name = 2
    elif name == "lizard":
        name = 3
    elif name == "scissors":
        name = 4
    else:
        name = "Error: invalid name"
    return name   

def number_to_name(number): # Converts number to name
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        name = "Error: Invalid number"
    return name

import random 

def rpsls(player_choice):
    print "\nPlayer chooses " + player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + comp_choice
    difference = (comp_number - player_number) % 5
    
    if difference == 1 or difference == 2:
        print "Computer wins!"
    elif difference == 0:
        print "Player and computer tie!"
    else:
        print "Player wins!"
    
# tests

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



