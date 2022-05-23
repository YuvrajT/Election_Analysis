#Adding dependencies
import os

import csv

#Assigned a variable to load a file from path 

file_to_load = os.path.join("Resources","election_results.csv")

#Assigned a variable to save the file to path

file_to_save = os.path.join("Analysis", "election_analysis_PyPoll.txt")

#1. Initialising the total vote counter

total_votes = 0 

#Candidate options and Candidate votes

candidate_options = []

#Declaring the empty dictionary

candidate_votes = {}

#Winng Candidate and Winning count tracker

winning_candidate = ""

winning_count = 0 

winning_percentage = 0 

#Open the elections results and read the file

with open(file_to_load) as election_data:

    #To read and analyse the elections data

    file_reader = csv.reader(election_data)

    #To print the header 

    headers = next(file_reader)

    print(headers)

    #to print the each row in CSV file 

    for row in file_reader:

        #Adding the total vote count
        
        total_votes += 1

        #Printing the candidatename from each row

        candidate_name = row[2]
    
        #Adding the candidate name tp list

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            #Begin tracking candidate's vote count

            candidate_votes[candidate_name] = 0 

        #Adding the vote count to candidate name

        candidate_votes[candidate_name] += 1

    #Save the results to text file 

with open(file_to_save, "w") as txt_file:

        elections_results = (
            f"\nElection Results\n"
            f"----------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"----------------------------\n")        

        print(elections_results, end="")

        txt_file.write(elections_results)

#Determining the % of votes for each candidate

#Iterating through the candidate list:

for candidate_name in candidate_votes:

#Retrieving vote count for candidate

    votes = candidate_votes[candidate_name]

    #Calculating the % of votes

    vote_percentage = float(votes) / float(total_votes) *100

    candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #Determining winning vote count and candidate

    if (votes > winning_count) and (vote_percentage > winning_percentage):

    #If true then set winning_count = votes and winning percentage
    # = vote percentage

        winning_count = votes

        winning_percentage = vote_percentage

        #set the winning candidate = to the candidate name

        winning_candidate = candidate_name


    #Printing the winning candidates results:

        winning_candidate_summary = (
            f"---------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentae: {winning_percentage:.1f}%\n"
            f"----------------------------\n")

    print(winning_candidate_summary) 

    #Save the winning detials to text file:
     
txt_file.write(winning_candidate_summary)       


