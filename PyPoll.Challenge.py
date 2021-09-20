 #-*- coding: UTF-8 -*-
"""PyPoll Homework Challenge"""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.

county_list = []


# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
#     # Print each row in the CSV file.

    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate...
        if county_name not in county_list:
            # Add it to the list of candidates.
            county_list.append(county_name)

### Print the county list that holds the names of the counties.
print(county_list)

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
county_list = []
# 1. Declare the empty dictionary.
county_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        county_name = row[1]

        if county_name not in county_list:
          # Add the candidate name to the candidate list.
            county_list.append(county_name)

           # 2. Begin tracking that candidate's vote count.
            county_votes[county_name] = 0

            # Add a vote to that candidate's count.
        county_votes[county_name] += 1


### Print the county vote dictionary. Holds the county as key and the votes cast for each county as the values
print(county_votes)

for county_name in county_votes:
    # 2. Retrieve vote count of a candidate.
    votes = county_votes[county_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
###### percentages
    print(f"{county_name}: received {vote_percentage}% of the vote.")

# Track the winning candidate, vote count and percentage
winning_county = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
    for county_name in county_votes:
    # Retrieve vote count of a candidate.
        votes = county_votes[county_name]
    # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
        ##print(f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
# 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
     # 2. If true then set winning_count = votes and winning_percent =
     # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
     # 3. Set the winning_candidate equal to the candidate's name.
            winning_county= county_name
        winning_county_summary = (
            f"-------------------------\n"
            f"Winner: {winning_county}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
print(winning_county_summary)
# 2: Track the largest county and county voter turnout.

#### CANDIDATE ANALYSIS
# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    print(total_votes)

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name


winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
txt_file.write(winning_candidate_summary)

  
