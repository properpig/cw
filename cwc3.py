# Filename: cwc3.py
# Name: Heng U San
# Centre No / Index No: 3024
# Description: Display all records that have not been returned, with a count of
# the total number of CDs and DVDs on loan

import datetime
import time

def PRINTRECORD():
    
    try:
        #open resource file for input
        resource_file = open("RESOURCE.DAT", "r")

        #read and skip first line
        heading_line = resource_file.readline()

        #read resource details
        resource_details = resource_file.readlines()

        #open loan file for input
        loan_file = open("LOAN.DAT", "r")
        
        #read loan details
        loan_details = loan_file.readlines()

        #remove the records that have been returned
        for record in loan_details:
            #check if the resource is returned
            if record[46:96] != " "*50:
                loan_details.remove(record)

        #obtain earliest and latest date due back
        earliest_datedueback = datetime.datetime.strptime(loan_details[0][40:46], "%d%m%y")
        latest_datedueback = datetime.datetime.strptime(loan_details[len(loan_details)-1][40:46], "%d%m%y")

        #create dictionary to store resource details
        resource_info = {}
        for record in resource_details:
            if record[41] == 'C':
                resource_type = "CD"
            else:
                resource_type = "DVD"
            resource_info[record[0:5]] = [record[5:30].rstrip(" "), resource_type]

        #create a temporary list to store loan details pertaining to a particular date due back
        temporary_list = []

        #initialize the record index
        record_index = 0

        #initialize the total number of CDs and DVDs on loan
        total_CDs_on_loan = 0
        total_DVDs_on_loan = 0

        #loop through each date in between the earliest and latest due dates
        for date in range(0, (latest_datedueback - earliest_datedueback).days+1):
            date_due_back = earliest_datedueback + datetime.timedelta(date)
            date_due_back.ctime()

            #print the current date
            print("Date: ", date_due_back.strftime("%d-%m-%Y"))
            print("-" * 75)
            
            date_due_back = date_due_back.strftime("%d%m%y")
            
            #obtain loan resource information for each record for the given date
            next_date = False
            #initialize the number of CDs and DVDs on loan for this date
            CDs_on_loan = 0
            DVDs_on_loan = 0
            while not next_date and record_index < len(loan_details):
                #loop through loan details and check if the laon due date matches this date
                if loan_details[record_index][40:46] == date_due_back:
                    resource_no = loan_details[record_index][0:5]
                    student_id = loan_details[record_index][5:10]
                    student_name = loan_details[record_index][10:40].rstrip(" ")
                    resource_title = resource_info[resource_no][0]
                    resource_type = resource_info[resource_no][1]
                    #append loan resource information to the temporary list
                    temporary_list.append([resource_no, resource_title, resource_type, student_id, student_name])
                    #update count of CDs or DVDs on loan
                    if resource_type == "CD":
                        CDs_on_loan = CDs_on_loan + 1
                    else:
                        DVDs_on_loan = DVDs_on_loan + 1
                    #move on to the next record
                    record_index = record_index + 1
                else:
                    #print out loan information for the current date due back
                    for resource in temporary_list:
                        print(resource[0], " "*5, resource[1], resource[2], resource[3], resource[4])
                    print("Number of resources: CD: ", CDs_on_loan, " DVD: ", DVDs_on_loan)
                    print()
                    #re-initialize temporary list
                    temporary_list = []
                    #update total number of CDs and DVDs on loan
                    total_CDs_on_loan = total_CDs_on_loan + CDs_on_loan
                    total_DVDs_on_loan = total_DVDs_on_loan + DVDs_on_loan
                    next_date = True
                    

        #print out loan information for the last date due back
        for resource in temporary_list:
            print(resource[0], " "*5, resource[1], resource[2], resource[3], resource[4])
        print("Number of resources: CD: ", CDs_on_loan, " DVD: ", DVDs_on_loan)
        print()

        #update total number of CDs and DVDs on loan
        total_CDs_on_loan = total_CDs_on_loan + CDs_on_loan
        total_DVDs_on_loan = total_DVDs_on_loan + DVDs_on_loan

        #print the total number of CDs and DVDs on loan
        print("Total number of resources: CD: ", total_CDs_on_loan, " DVD: ", total_DVDs_on_loan)
                        
        #close files
        loan_file.close()
        resource_file.close()  

    except IOError:
        #Display file input and output error
        print("Error! Cannot read from input file or write to output file.")

#main
if __name__ == "__main__":
    PRINTRECORD()
