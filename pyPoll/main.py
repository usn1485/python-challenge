import os
import csv

# Path to collect data from the Resources folder
Election_Data = os.path.join('election_data.csv')

electiondata={}
totalVotes=0
candidates=[]
percentage={}
winner=""
winning_count=0
line=""
 
def output(lines):
    global line
    line=f'{line}\n{lines}'
    

# Read from the CSV file
with open(Election_Data, 'r') as csvfile:
     
    # Split the data on commas
   
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        totalVotes= totalVotes+1
        name=row[2]             
        if name not in candidates:
            candidates.append(name)
            electiondata[name]=0
        electiondata[name] +=1  

 
output(
f"""Election Results
----------------------------------------
Total Votes: {totalVotes}
----------------------------------------"""
)    
       
    
for key, value in electiondata.items():
        percentage[key] =round((electiondata[key]/totalVotes)*100,2)
        if winning_count < value:
            winning_count = value
            winner = key
        output(f' {key}:{percentage[key]}% ({electiondata[key]})')
         
output(f'----------------------------------------\nWinner: {winner} \n----------------------------------------') 
 
output_file = os.path.join("Election_data_Analysis.txt")

#  Open the output file
with open(output_file, "w") as datafile:
    datafile.write(line)
    

     
               
   
        

         
      
