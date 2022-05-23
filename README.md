# Election Analysis

## Overview of Election Audit

### Purpose:

Analyze election data for the state of Colorado in three different counties i.e. Jeffeson, Denever and Arapahoe and to determine the winning candidate.

### Election Audit Results:

- Total number of votes cast in congressional election are 369,711

![](https://github.com/YuvrajT/Election_Analysis/blob/main/Resources/Total%20Vote.png)

#### Breakdown of Votes for each county:

- County Jefferson received total votes of 38,855 which was at 10.5% of the total votes casted in election.

- County Denver received the **highest votes** among all counties, a total of 306,055 i.e. 82.8% of total votes casted.

- County Arapahoe received the lowest votes, 24,801 i.e. 6.7% of the total votes.

- Using the for loop I was able to county individual county votes

![](https://github.com/YuvrajT/Election_Analysis/blob/main/Resources/County.png)

#### Breakdown of votes for each Candidate:

- Starting with candidate Charles Casper Stockham they received 85,213 votes which was 23.0% of the total votes.

- Candidate Diana Degette got the **highest vote and is the winning candidate** of the election: she received 272,892 votes which is 73.8% of the total votes.

- Lastly, candidate Raymon Anthony Doane received the lowest votes among other two candidates votes counting to only 11,606 (3.1%) of votes. 

- Using the for loop again, I was able to county individual votes for the candidate

![](https://github.com/YuvrajT/Election_Analysis/blob/main/Resources/Candidate.png)

### Audit Summary:

I have written the python script, keeping in mind that there will be future use of the scrit. You will be be able to understand my code by reading the comments before every line of code. if siutatuon persists and you require additional information, I have listed two possible examples below:

This python code sript can be utlisied in many different ways depending on situation. If the situation comes and you have to analyse other counties election data you will have provide the correct path to the CSV file in highlighted part in below code. Ensure the new CSV file is the same format as the current one and you will be able to get the same results for the new election data. 

![](https://github.com/YuvrajT/Election_Analysis/blob/main/Resources/File_Path.png)

If the situation comes and you have to analyse the data for just candidates, not for counties and find out the winning candidate you can chose to comment out the code from line 23-24, 33-34 and 102-139. 

![](https://github.com/YuvrajT/Election_Analysis/blob/main/Resources/Lines%20.png) 
![](https://github.com/YuvrajT/Election_Analysis/blob/main/Resources/File%20path%203.png)
![](https://github.com/YuvrajT/Election_Analysis/blob/main/Resources/File%20path%202.png)



