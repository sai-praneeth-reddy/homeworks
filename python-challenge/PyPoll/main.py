# Location of the csv file - EDIT THE PATH BELOW WHEN RUNNING THE PROGRAM

file = '/Users/saireddy/Desktop/election_data.csv'

# Location to export the text file - EDIT THE PATH BELOW WHEN RUNNING THE PROGRAM

file2 = '/Users/saireddy/Desktop/Py_Poll.txt'

# Creating a empty list that would hold the columns read from the csv file

voter_id = []

candidate_list_duplicate = []

candidate_list_unique = []

# Read the csv file

import csv

with open(file, 'r') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=",")

    # Move the IO the row after Header

    csv_header = next(csv_reader)

    # Store the columns of the csv file in the above created empty lists

    for row in csv_reader:

        voter_id.append(row[0])

        candidate_list_duplicate.append(row[2])


#1. The total number of votes cast

def total_votes():

    Total = 0

    for _ in voter_id:

        Total = Total + 1

    return Total
    
    
total_votes = total_votes()


output1  = "Total Votes: " + str(total_votes)

print(output1)

with open(file2, 'w') as text:

    text.write(output1 + '\n')

  

#2 A complete list of candidates who received votes

def candidate_list():

    for row in candidate_list_duplicate:

        if row not in candidate_list_unique:

            candidate_list_unique.append(row)

candidate_list()

#print (candidate_list_unique)



#3 and 4 Total number of votes each candidate won and percentage of votes


# Empty dictionary to hold total votes for each candidate

total_votes_cand = {}


for i in candidate_list_unique:

    total_votes_cand[i] = 0  
    

with open(file, 'r') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=",")

    # Move the IO the row after Header

    csv_header = next(csv_reader)

    for row in csv_reader:

        total_votes_cand[row[2]] += 1  

def percentages():

    with open(file2, 'a') as text:

        for i in candidate_list_unique:
    
            percentage_votes = (total_votes_cand[i]/total_votes) * 100

            output_i =  str(i) + ":" + str(percentage_votes) + "%" + "(" + str(total_votes_cand[i]) + ")"

            print(output_i)

            text.write(output_i + '\n')

percentages()



#5 The winner of the election based on popular vote.


# Create an empty list to hold the total votes of all candidates 

total_votes_list = []

for row in candidate_list_unique:

    total_votes_list.append(total_votes_cand[row])


#Get the winner

def winner():

        max_votes = 0

        for i in range(0, len(total_votes_list)-1):

            if total_votes_list[i] > max_votes:

                max_votes = total_votes_list[i]

                winner_index = total_votes_list.index(max_votes)

                winner = candidate_list_unique[winner_index]

        return "Winner:" + winner

winner_of_elec = winner()

print(winner_of_elec)

# Output to text file

with open(file2, 'a') as text:

    text.write(winner_of_elec)







    
























    

        

