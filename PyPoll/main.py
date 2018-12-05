from time import time
import csv as csv
import os as os
start_time = time()
dictCandidate = {} 
var_counter = 0
var_votes = 0
var_winner = ""

csv_path = os.path.join("election_data.csv")
with open(csv_path, 'r', ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:      
        var_votes = dictCandidate.get(row[2], 0)
        var_votes += 1 
        dictCandidate[row[2]] = var_votes
        var_counter += 1
var_winner = sorted(dictCandidate, key=dictCandidate.__getitem__, reverse= True) [0]
print("Election Results")        
print("-------------------------")  
print(f"Total Votes:{var_counter}")  
print("-------------------------")
for key, value in dictCandidate.items():
    print(f"{key}:", end = '')
    print('{0:.3f}'.format((value/var_counter)*100),end = '')
    print("%", end = '')
    print(f" ({value})")
print("-------------------------")
print(f"Winner:{var_winner}")  
print("-------------------------")
elapsed_time = time() - start_time
print("Elapsed time: %0.10f seconds." % elapsed_time)
# Specify the file to write to
output_path = os.path.join("salida2.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtFile:
#We use the new prinf method which is available from version 3.0    
    print("Election Results", file = txtFile)        
    print("-------------------------", file = txtFile)  
    print(f"Total Votes:{var_counter}", file = txtFile)  
    print("-------------------------", file = txtFile)
    for key, value in dictCandidate.items():
        print(f"{key}:", end = '', file = txtFile)
        print('{0:.3f}'.format((value/var_counter)*100),end = '', file = txtFile)
        print("%", end = '', file = txtFile)
        print(f" ({value})", file = txtFile)
    print("-------------------------", file = txtFile)
    print(f"Winner:{var_winner}", file = txtFile)  
    print("-------------------------", file = txtFile)