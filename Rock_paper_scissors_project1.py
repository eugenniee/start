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

import random

def name_to_number(name):     # Converts name to number
    name = name.lower()
    if name == "rock":
        name = 0
    elif name == "spock":
        name = 1
    elif name == "paper":
        name = 2
    elif name == "lizard":
        name = 3
    elif name == "scissors":
        name = 4
    else:
        name = -1
    return name   

def number_to_name(number): # Converts number to name
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print "Error: Invalid number"
    return name

def rpsls(player_choice):
    print "\nPlayer chooses " + player_choice
    player_number = name_to_number(player_choice)
    
    if player_number < 0:
        print "Error: invalid name\n"
        return
    
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + comp_choice
    difference = (comp_number - player_number) % 5
    
    if difference == 1 or difference == 2:
        print "Computer wins!\n"
    elif difference == 0:
        print "Player and computer tie!\n"
    else:
        print "Player wins!\n"
    
# tests
while True:
    var = raw_input("Please enter your choice: ")
    rpsls(var)

#rpsls("rock")
#rpsls("Spock")
#rpsls("paper")
#rpsls("lizard")
#rpsls("scissors")
#rpsls("papr")



