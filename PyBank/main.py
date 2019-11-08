#Declare Dependencies
import os
import csv

#Define input file path
PyBank_csv = os.path.join("Resources", "budget_data.csv")

#initialize variables
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

#open File
with open(PyBank_csv, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Skips the header row
    next(csvreader, None)

    # Read each row of data after the header
    for row in csvreader:
        
        #Stores the current month's Profit/Loss
        curP = float(row[1])
        

        #if this is the first run of the loop, then store the company's starting profit 
        if (tFirst == 0):
            #store the first value for our final calculations
            first = curP
            #store last to track the previously read values
            last = curP
            #change tFirst to 1 to not enter this section of the IF statement
            tFirst = 1
            #Since this is the first run, we have no previous data.  So the assumption is there is no change
            change = 0
        else:
            #if its not the first run, calculate the change in profit
            change = curP-last
            #store the current value into the previous value variable
            last = curP
        #increment the month counter
        months = months + 1
        #increment the total profit over the full period
        tot = tot + curP

        #if the change in profit is higher than the highest change or lower than the lowest change thus far, store this current change in the appropriate variable
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
 