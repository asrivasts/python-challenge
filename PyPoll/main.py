import os
import csv
from collections import Counter

#Set the input data path
PyPoll_csv = os.path.join("Resources", "election_data.csv")


#Create an empty list to store all of the votes
candidate = []

with open(PyPoll_csv, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Skips the header row
    next(csvreader, None)

    # Read each row of data after the header
    for row in csvreader:
        candidate.append(row[2])

#leverage Counter module to parse through the list, find unique candidates, and count their occurences
results = Counter(candidate)

#create a list of the number of votes each candidate received.  We wil use this list to sort and determine the winner based on most votes
votes = []
count = 0

#getting the actual votes from the results.  Adding the final tally of total votes collected
for i in results:
    votes.append(results[i])
    count += results[i]

#leveraging the built-in sorting capabilities to sort highest to lowest
votes.sort(reverse = True)
winner = ""

print("\nElection Results")
print("-------------------------")
print("Total Votes: " + str(count))
print("-------------------------")

for i in range(len(votes)):
    for name, numVotes in results.items():    # for name, number of Votes in results  
        if votes[i] == numVotes:              # based on the current sorted votes list, find the candidate that has that vote count.  Short-coming in this is when two candidates have the same number of votes
            numVotes = format(numVotes, ",")    #formatting for prettier output
            percent = format(votes[i]/count, "0.3%")    #formatting for prettier output
            print(f"{name}: {percent} ({numVotes})")    #printing the required information
            if i ==0:
                winner = name   #because we sorted from highest to lowest, the winner is the first person's name we find in votes
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")