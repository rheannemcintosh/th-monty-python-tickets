# ---------------------------------------------------------------- #
#
# masterticket.py
# 
# This is a sample project created to purchase tickets for a Monty
# Python show via the command line. Built in conjuntion with the
# Python Basics course at teamtreehouse.com
#
# Author:  Rheanne McIntosh <rheanne.mcintosh@outlook.com>
# Created: November 2020
#
# ---------------------------------------------------------------- #

# Declare a constants and variables
TICKET_PRICE      = 10
tickets_remaining = 100

# Output how many tickets are remaining
print("There are {} tickets remaining.".format(tickets_remaining))

# Gather input for the users name
name = input("What is your name? ")

# Prompt the user by name and ask how many tickets they would like
num_tickets = input("How many tickets would you like, {}? ".format(name))
num_tickets = int(num_tickets)

# Calculate the price and assign it to a variable
amount_due = num_tickets * TICKET_PRICE

# Ouput the price to the screen
print("The totla due is £{}".format(amount_due))