import os
import csv

# Path to collect data from the Resources folder
budgetData = os.path.join('budget_data.csv')

# Read from the CSV file
with open(budgetData, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader,None)
    count=0
    totalAmount=0
    Months=['Jan','Feb','Mar','Apr','May','Jun','Jul',
     'Aug','Sept','Oct','Nov','Dec']

    Month=[]

    for row in csvreader:
        print(row)    
        date=((row[0].split('-')))
        #Month.append(date[3])
        Month= (date[0]) 
        if Month in Months:
            count= count+1
            totalAmount= totalAmount + int(row[1])
    
    print(f'count is: {count}')
    print(f'total amount is :{totalAmount}')

