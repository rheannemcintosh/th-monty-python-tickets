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

# Declare constants and variables
SERVICE_CHARGE    = 2
TICKET_PRICE      = 10
tickets_remaining = 100

# Calculate price function
def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

# Run a loop to allow users to buy tickets
while tickets_remaining >= 1:

    print("There are {} tickets remaining.".format(tickets_remaining))

    name        = input("What is your name? ")
    num_tickets = input("How many tickets would you like, {}? ".format(name))

    try:
        num_tickets = int(num_tickets)
        
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    
    except ValueError as err:
        print("Oh no, we ran into an issues. {}. Please try again!".format(err))
    
    else:
        amount_due = calculate_price(num_tickets)
        print("The total due is £{}".format(amount_due))
        should_proceed = input("Do you want to proceed? (Y/N) ")

        if should_proceed.lower() == "y":
            print("SOLD!")
            tickets_remaining -= num_tickets
        else:
            print("Thank you anyway, {}!".format(name))

print("Sorry the tickets are all sold out!")