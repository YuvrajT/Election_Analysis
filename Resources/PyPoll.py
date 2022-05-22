#Adding dependencies
import os

import csv

#Assigned a variable to load a file from path 

file_to_load = os.path.join("Resources","election_results.csv")

#Assigned a variable to save the file to path

file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Open the elections results and read the file

with open(file_to_load) as election_data:

    #To read and analyse the elections data

    file_reader = csv.reader(election_data)

    #To print the header 

    headers = next(file_reader)

    print(headers)