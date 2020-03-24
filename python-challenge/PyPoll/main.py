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

    return "Total Votes:" + str(Total)

output1 = total_votes()

print(output1)


# A complete list of candidates who received votes

def candidate_list():

    for row in candidate_list_duplicate:

        if row not in candidate_list_unique:

            candidate_list_unique.append(row)

candidate_list()

#print (candidate_list_unique)


##########################################  WORK ON IMPROVING THE BELOW CODE - IT IS NOT SCALABLE   ######################################


# Count the number of votes and percentage of votes for each candidate

# An Empty list to store the voter ID for each candidate

cand1_list = []

cand2_list = []

cand3_list = []

cand4_list = []

def total_votes2():

    Total = 0

    for _ in voter_id:

        Total = Total + 1

    return Total

total_votes = total_votes2()

with open(file, 'r') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=",")

    # Move the IO the row after Header

    csv_header = next(csv_reader)

    for row in csv_reader:

        if row[2] == candidate_list_unique[0]:

            cand1_list.append(row[0])

            total_cand1 = len(cand1_list)

            percentage_cand1 = (total_cand1)/(total_votes) * 100

        
        elif row[2] == candidate_list_unique[1]:

            cand2_list.append(row[0])
    
            total_cand2 = len(cand2_list)

            percentage_cand2 = (total_cand2)/(total_votes) * 100

    
        elif row[2] == candidate_list_unique[2]:

            cand3_list.append(row[0])
    
            total_cand3 = len(cand3_list)

            percentage_cand3 = (total_cand3)/(total_votes) * 100


        elif row[2] == candidate_list_unique[3]:

            cand4_list.append(row[0])
    
            total_cand4 = len(cand4_list)

            percentage_cand4 = (total_cand4)/(total_votes) * 100

# Determine the winner

    count_list = [total_cand1, total_cand2, total_cand3, total_cand4]

    def winner():

        max_votes = 0

        for value in count_list:

            if value > max_votes:

                max_votes = value

                winner_index = count_list.index(max_votes)

                winner = candidate_list_unique[winner_index]

        return "Winner:" + winner

    winner_of_elec = winner()

    
    # Output the results to terminal

    output_cand1 = str(candidate_list_unique[0]) + ":" + str(percentage_cand1) + "%" + "(" + str(total_cand1) + ")"

    output_cand2 = str(candidate_list_unique[1]) + ":" + str(percentage_cand2) + "%" + "(" + str(total_cand2) + ")"

    output_cand3 = str(candidate_list_unique[2]) + ":" + str(percentage_cand3) + "%" + "(" + str(total_cand3) + ")"

    output_cand4 = str(candidate_list_unique[3]) + ":" + str(percentage_cand4) + "%" + "(" + str(total_cand4) + ")"

    print(output_cand1)

    print(output_cand2)

    print(output_cand3)

    print(output_cand4)

    print(winner_of_elec)

# Write all the required outputs to text file


with open(file2, 'w') as text:

    text.write(output1 + '\n')

    text.write(output_cand1 + '\n')

    text.write(output_cand2 + '\n')

    text.write(output_cand3 + '\n')

    text.write(output_cand4 + '\n')

    text.write(winner_of_elec + '\n')

    


    
    














    

        

