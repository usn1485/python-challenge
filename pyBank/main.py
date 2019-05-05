import os
import csv

# Path to collect data from the Resources folder
budgetData = os.path.join('budget_data.csv')

count,count1=0,0
totalAmount=0
totalchange=0
track_change=0
Month=""
Dates=[]
changeInPL=[]
pl_List=[]
line=""

def output(lines):
    global line
    line=f'{line}\n{lines}'

# Read from the CSV file
with open(budgetData, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader,None)  #skip the header
    

    Months=['Jan','Feb','Mar','Apr','May','Jun','Jul',  # create a Month array
     'Aug','Sep','Oct','Nov','Dec']
       
    for row in csvreader:            #read CSV data
          
        date=((row[0].split('-')))            #get the date and split it 
        Dates.append(date)                  
        Month= (date[0])                     # extract Month from Date object
         
        if Month in Months:                  #check if Month of that row is in Months list
            count +=1                        # countercount the no of months
            totalAmount= totalAmount + int(row[1])     #count the total amount by adding amount from each row
        pl_List.append(row[1])               
        
    for i in range(len(pl_List)-1):
        count1 +=1
        changeInPL.append(int(pl_List[i+1])-int(pl_List[i]))
        totalchange += int(changeInPL[i])
     
    avarage =str(round(totalchange/count1,2))
    MaxChange=max(changeInPL)
    MinChange=min(changeInPL)
    indexofMaxChange=changeInPL.index(MaxChange)+int(1)
    dateofMax=Dates[indexofMaxChange]
    indexOfMinChange=changeInPL.index(MinChange)+int(1)
    dateOfMin=Dates[indexOfMinChange]

   
    
    output(f"""
     ---------------------------- \n      
     Finanacial Analysis \n
     ----------------------------\n
     Total Months:  ${count}\n
     Total: ${totalAmount}\n
     Avarage Change: ${avarage}\n
     Greatest Increase in profits :{dateofMax}  {MaxChange}\n
     Greatest Decrease in profits :{dateOfMin}  {MinChange} \n
    --------------------------------------------------------""")

output_file = os.path.join('Budget_data_Finanacial_Analysis.txt')
#  Open the output file
with open(output_file, "w") as datafile:
    datafile.write(line)


     

    

    


