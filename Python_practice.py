# # How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
# #  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100

# if (percentage_votes > 50.1 then print "WON"


# print(f"I received {percentage_votes} % of the total votes.")

# from typing import Counter


from tkinter import Y


counties = ["Arapahoe","Denver","Jefferson"]
# if counties[2] == 'Denver':
#     print(counties[2])

# temperature = int(input("what is the temperature outside ?"))

# if temperature >= 80:
#     print("Turn on the AC")
# else:
#     print("Go outside")

# What is the score ?

# score = int(input("Enter your test score to find out your grade: "))

# if score >= 90:
#     print("Your grade is an A")
# else:
#     if score >= 80:
#         print("Your grade is B")
#     else:
#         if score >= 70:
#             print("Your grade is C")
#         else:
#             if score >= 60:
#                 print("Your grade is D")
#             else:
#                 print("FAIL")

# if score >= 90:
#     print("Your grade is an A")
# elif score >= 80:
#     print("Your grade is B")
# elif score >= 70:
#     print("Your grade is C")
# elif score >= 60:
#     print("Your grade is D")
# else:
#     print("FAIL")              


## Membership Operators

# countries = ["India", "Canada", "US"]

# if "India" in countries:
#     print ("True")
# else:
#     print("False")

# if "Montreal" not in countries:
#     print ("Montreal is not in countries")
# else:
#     print("Montreal is in countries")

## Logical Operatos

# x = 5
# y = 9

# if not(x>=y):
#     print ("True")
# else:
#     print("False")

# x = 6
# while x <= 7:
#     print(x)
#     x = x + 1

# for a in counties:
#     print(a)


# number = (0,1,2,3,4,5,6)
# for a in range(9):
#     print(a)


# for b in range(len(counties)):
#     print(b)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for c in counties_dict.keys():
#     print(c)

# for c in counties_dict.values():
#     print(c)

# for c in counties_dict.keys().Values():
#     print(c)

# for c in counties_dict:
#     print(counties_dict[c])

# for c in counties_dict:
#     print(counties_dict.get(c))

# for a, b in counties_dict.items():
#     print(f"{a} county has {b} registered voters.")

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},   
#                {"county":"Denver", "registered_voters": 463353}, 
#                 {"county":"Jefferson", "registered_voters": 432438}]

# voting_data = {"county":"Arapahoe", "registered_voters": 422829}
# # print(voting_data)    

# # for g in voting_data:
# #     print(g)

# print(f"{voting_data['county']['registered_voters']}")



# for x in range(9):
#     print(x)

# range_list = list(range(5))
# print (range_list)

# word = "Peace"

# for i in word:
#     print(i)

# zoo = ["cat", "dog", "rabbit"]

# for b in zoo:
#     print (b)

run = "y"

while run == "y":
    print("start understanding the logic")
    run = input("to run again, Enter y")


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

# 3 ways to open a csv file 
#1. Indirect way: when you dont know th path 

# import os

# import csv


# cwd = os.getcwd()
# print(f"current working directory: {cwd}")
# csvpath = os.path.join("Resources","election_results.csv")
# print(f"path is: {csvpath}")

# with open(csvpath) as election_file:

#     csvreader = csv.reader(election_file, delimiter = ",")
    
#     print(csvreader)

#2. Direct when you know the path using with 

# file = "Resources/election_results.csv"

# with open(file) as election_data:

#     print(election_data)

# import os

# import csv


# cwd = os.getcwd()
# print(f"current working directory: {cwd}")
# file_to_load = os.path.join("Resources","election_results.csv")
# file_to_save = os.path.join("Analysis", "election_analysis.txt")

# print(f"path is: {csvpath}")

# # with open(csvpath) as election_file:

# #     csvreader = csv.reader(election_file, delimiter = ",")
    
# #     print(csvreader)

# file_to_save = os.path.join("Analysis", "election_analysis.txt")

# with open(file_to_save, "w") as text_file:

#     countires = (f"Counties in the Election\n"
#                 f"---------------------------\n"
#                 f"Arapahoe\nDenver\nJefferson")

#     text_file.write(countires)