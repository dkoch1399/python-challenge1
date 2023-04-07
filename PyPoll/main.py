import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")

with open(election_data_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    votes_cast = 0
    candidate_votes = {}
    candidate_won = ""
    count_won = 0
    for row in csv_reader:
        votes_cast += 1
        candidate_name = row[2]
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
        else:
            candidate_votes[candidate_name] += 1
        if candidate_votes[candidate_name] > count_won:
            candidate_won = candidate_name
            count_won = candidate_votes[candidate_name]
    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {votes_cast}")
    print("------------------------") 
    for candidate, votes, in candidate_votes.items():
        percent_votes = votes / votes_cast * 100 
        print(f"{candidate}: {percent_votes:.3f} {votes}")
    print("------------------------")
    print(f"Winner: {candidate_won}")
    print("------------------------")