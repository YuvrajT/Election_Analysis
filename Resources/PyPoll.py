# The Data we need to retrieve. 
# Total number of votes cast.
# A complete list of candidates who received votes.
# Total number of votes each candidate received.
# Percentage of votes each candidate won.
# The winner of the election based on popular vote.

# Import the datetime class from datetime moduel 

# import datetime as dt

#Use the now() attribute on the datetime class to get the present time.

# now = dt.datetime.now()

# # Print the present time.

# print("The time right now is ", now)

# import csv

# dir(csv)

# import csv
# import os
# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("/Users/yuvraj/Election_Analysis/Resources/election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Print the file object.
#      print(election_data)


# Incorporate the random library
# import random

# # Print Title
# print("Let's Play Rock Paper Scissors!")

# # Specify the three options

# options = ["r", "p", "s"]

# continue_playing = "y"

# while continue_playing == "y":




# # Computer Selection
#     computer_choice = random.choice(options)    

# # User Selection
#     user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# # Run Conditionals
#     if (user_choice == "r" and computer_choice == "p"):
#         print("You chose rock. The computer chose paper.")
#         print("Sorry. You lose.")

#     elif (user_choice == "r" and computer_choice == "s"):
#         print("You chose rock. The computer chose scissors.")
#         print("Yay! You won.")

#     elif (user_choice == "r" and computer_choice == "r"):
#         print("You chose rock. The computer chose rock.")
#         print("A smashing tie!")

#     elif (user_choice == "p" and computer_choice == "p"):
#         print("You chose paper. The computer chose paper.")
#         print("A smashing tie!")

#     elif (user_choice == "p" and computer_choice == "s"):
#         print("You chose paper. The computer chose scissors.")
#         print("Sorry. You lose.")

#     elif (user_choice == "p" and computer_choice == "r"):
#         print("You chose paper. The computer chose rock.")
#         print("Yay! You won.")

#     elif (user_choice == "s" and computer_choice == "p"):
#         print("You chose scissors. The computer chose paper.")
#         print("Yay! You won.")

#     elif (user_choice == "s" and computer_choice == "s"):
#         print("You chose scissors. The computer chose scissors.")
#         print("A smashing tie!")

#     elif (user_choice == "s" and computer_choice == "r"):
#         print("You chose scissors. The computer chose rock.")
#         print("Sorry. You lose.")

#     else:
#         print("I don't understand that!")
#         print("Next time, choose from 'r', 'p', or 's'.")

#     continue_playing = input("Continue playing ? Enter y or n ?")


# # Initial variable to track game play
# user_play = "y"

# # While we are still playing...
# while user_play == "y":

#     # Ask the user how many numbers to loop through
#     user_number = int(input("How many numbers? "))

#     # Loop through the numbers. (Be sure to cast the string into an integer.)
#     for x in range(user_number):

#         # Print each number in the range
#         print(x)

#     # Once complete...
#     user_play = input("Continue: (y)es or (n)o? ")

# Initial variable to track game play
# user_play = "y"

# # While we are still playing...

# start_number = 0 

# while user_play == "y":

#     # Ask the user how many numbers to loop through
    
#     user_number = int(input("How many number you want me to print ?"))

#     # Loop through the numbers. (Be sure to cast the string into an integer.)
    
#     for i in range(start_number, user_number + start_number):
    
#     # Print each number in the range
       
#         print(i)

#     start_number = start_number + user_number

#     # Once complete...
#     user_play = input("Continue: (y)es or (n)o? ")



import os

import csv


cwd = os.getcwd()
print(f"current working directory: {cwd}")
csvpath = os.path.join("Resources","election_data")
print(f"path is: {csvpath}")

# with open(csvpath) as electionfile:

# csvreader = csv.reader(electionfile, delimiter = " ")



   