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

# Run this code until we run ouy of tickets
while tickets_remaining >= 1:

    # Output how many tickets are remaining
    print("There are {} tickets remaining.".format(tickets_remaining))

    # Gather input for the users name
    name = input("What is your name? ")

    # Prompt the user by name and ask how many tickets they would like
    num_tickets = input("How many tickets would you like, {}? ".format(name))

    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issues. {}. Please try again!".format(err))
    else:

        # Calculate the price and assign it to a variable
        amount_due = num_tickets * TICKET_PRICE

        # Ouput the price to the screen
        print("The total due is £{}".format(amount_due))

        # Prompt the user if they want to proceed
        should_proceed = input("Do you want to proceed? (Y/N) ")

        # If they want to proceed
        if should_proceed.lower() == "y":

            # Print SOLD! and reduce number of tickets
            print("SOLD!")
            tickets_remaining -= num_tickets

        # Else
        else:

            # Thank by name
            print("Thank you anyway, {}!".format(name))

# Notify the user that the tickets or sold out
print("Sorry the tickets are all sold out!")