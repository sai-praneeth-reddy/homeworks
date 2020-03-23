# Location of the csv file - EDIT THE PATH BELOW WHEN RUNNING THE PROGRAM

file = '/Users/saireddy/Desktop/budget_data.csv'

# Location to export the text file - EDIT THE PATH BELOW WHEN RUNNING THE PROGRAM

file2 = '/Users/saireddy/Desktop/Py_Bank.txt'

# Creating a empty list that would hold the columns read from the csv file

date_list = []

num_list = []

change_list = []


# Read the csv file

import csv

with open(file, 'r') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=",")

    # Move the IO the row after Header

    csv_header = next(csv_reader)

    # Store the columns of the csv file in the above created empty lists

    for row in csv_reader:

        date_list.append(row[0])

        num_list.append(row[1])

#print(date_list)

#print(num_list)

#1. The total number of months included in the dataset

def months():

    total_months = 0

    for _ in date_list:

        total_months = total_months + 1

    #return print(f'Total Months:{total_months}') 

    return "Total Months: $" + str(total_months)


output1 = months()

# Write the output to terminal and text file

print(output1)

with open(file2, 'w') as text:

    text.write(output1 + '\n')


#2. The net total amount of "Profit/Losses" over the entire period

def total():

    total_amount = 0

    for row in num_list:

        total_amount = total_amount + int(row)

    return "Total: $" + str(total_amount)

output2 = total()

# Write the output to terminal text file

print(output2)

with open(file2, 'a') as text:

    text.write(output2 + '\n')



# Compute the month to month change in profit/losses

def change():

    for i in range (0, len(num_list) - 1):

        change = float(num_list[i+1]) - float(num_list[i])

        change_list.append(change)

change()


#print(change_list)


#3. The average of the changes in "Profit/Losses" over the entire period

def average():

    n = len(change_list)

    total = 0

    for row in change_list:

        total = total + row

        average_change = total/n

    return "Average Change:$" + str(average_change)

output3 = average()

# Write the output to terminal and text file

print(output3)

with open(file2, 'a') as text:

    text.write(output3 + '\n')


#4. The greatest increase in profits (date and amount) over the entire period

def gt_increase():

    greatest_increase = 0

    for row in change_list:

        if row > greatest_increase:

            greatest_increase = row

            # Getting the month in which the Gretest increase occures
            greatest_increase_index = change_list.index(greatest_increase)

            month_greatest_increase = date_list[greatest_increase_index + 1]

    
    return "Greatest increase in profits:" +  month_greatest_increase + "(" + "$" + str(greatest_increase) + ")"

output4 = gt_increase()

# Write the output to terminal and text file

print(output4)

with open(file2, 'a') as text:

    text.write(output4 + '\n')

#5. The greatest decrease in losses (date and amount) over the entire period


def gt_decrease():

    greatest_decrease = 0

    for row in change_list:

            if row < greatest_decrease:

                greatest_decrease = row

                # Getting the month in which the Gretest decrease occures

                greatest_decrease_index = change_list.index(greatest_decrease)

                month_greatest_decrease = date_list[greatest_decrease_index + 1]

    
    return "Greatest decrease in profits:" +  month_greatest_decrease + "(" + "$" + str(greatest_decrease) + ")"

output5 = gt_decrease()

# Write the output to terminal and text file

print(output5)

with open(file2, 'a') as text:

    text.write(output5 + '\n')










    





    















