import os
import csv

# Path to collect data from the Resources folder
budgetData = os.path.join('budget_data.csv')
#budgetData = os.path.join('C:/Users/Ujwala/Desktop/Washu/Python/python-challenge/pyBank/budget_data.csv')
#Get avarage of the changes in profit/losses 



# Read from the CSV file
with open(budgetData, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader,None)
    count=0
    count1=0
    totalAmount=0
    totalchange=0
    track_change=0
    Month=""
    changeInPL=[]
    pl_List=[]

    Months=['Jan','Feb','Mar','Apr','May','Jun','Jul',
     'Aug','Sep','Oct','Nov','Dec']
       
    for row in csvreader:
          
        date=((row[0].split('-')))
        Month= (date[0])
         
        if Month in Months:
            count= count+1    
            totalAmount= totalAmount + int(row[1])
        pl_List.append(row[1])
        
    for i in range(len(pl_List)-1):
        count1= count1+1
        track_change=(int(pl_List[i+1])-int(pl_List[i]))
        changeInPL.append(track_change)
        totalchange=totalchange + int(changeInPL[i])
                
    print(f'Length of pl :{len(pl_List)}')  
    print(f'Total Change:{totalchange}')
    print(f'Total count:{count1}')   
    avarage = float(totalchange/count1)
   
    print('----------------------------')        
    print ("Finanacial Analysis")
    print('----------------------------')
    print(f'Total Months:  {count}')
    print(f'Total: ${totalAmount}')
    print(f'Avarage Change:' "%.2f" % avarage)
    print(f'Greatest Increase :{max(changeInPL)}')
    print(f'Greatest Decrease :{min(changeInPL)}')


