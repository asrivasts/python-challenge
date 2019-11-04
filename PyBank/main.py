import os
import csv


PyBank_csv = os.path.join("Resources", "budget_data.csv")

months = 0
tot = 0
avg = 0
maxP = 0
maxL = 0
monthP = ""
monthL = ""
first = 0
last = 0
tFirst =0

with open(PyBank_csv, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Skips the header row
    next(csvreader, None)

    # Read each row of data after the header
    for row in csvreader:
        
        curP = float(row[1])
        

        if (tFirst == 0):
            first = curP
            last = curP
            tFirst = 1
            change = 0
        else:
            change = curP-last
            last = curP
        
        months = months + 1
        tot = tot + curP
        if (change > maxP):
            maxP = change
            monthP = row[0]
        if (change < maxL):
            maxL = change
            monthL = row[0]
  

# Format numbers for output
tot = format(tot, ',.2f')
avg = format((last-first)/months, ',.2f')  
maxP = format(maxP, ',.2f')
maxL = format(maxL, ',.2f')


#--------------------------------------------------------------
#Output to Terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${tot}")
print(f"Average  Change: ${avg}")
print(f"Greatest Increase in Profits: {monthP} ${maxP}")
print(f"Greatest Decrease in Profits: {monthL} ${maxL}")

#Output to File
output_file = os.path.join("output.txt")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w") as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("----------------------------\n")
    datafile.write(f"Total Months: {months}\n")
    datafile.write(f"Total: ${tot}\n")
    datafile.write(f"Average  Change: ${avg}\n")
    datafile.write(f"Greatest Increase in Profits: {monthP} ${maxP}\n")
    datafile.write(f"Greatest Decrease in Profits: {monthL} ${maxL}\n")
    datafile.write("----------------------------")
 