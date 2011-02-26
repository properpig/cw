# Filename: cwc2.py
# Name: Heng U San
# Centre No / Index No: 3024
# Description: Update LOAN.DAT after student evaluation is entered

def RETURNRESOURCE():

    try:
        #open loan file for reading
        loan_file = open("LOAN.DAT", "r")

        #read and process the details of the loan file
        loan_details = loan_file.readlines()

        #close loan file
        loan_file.close()

    except IOError:
        #output an error if the input file does not exist
        print("Error, input file does not exist.")

    try:
        #open loan file for writing
        loan_file = open("LOAN.DAT", "w")

        #set the number of updates made to zero
        no_of_updates = 0

        #run a loop until user is done with input
        finish_input = False
        while not finish_input:

            #get and validate resource number
            valid_resource_no = False
            while not valid_resource_no:
                resource_no = input("Enter resource number: ")
                if len(resource_no) == 0: #presence check
                    print("Error. Please enter something.")
                elif len(resource_no) != 5: #length check
                    print("Error, resource number must be exactly 5 characters.")
                elif not resource_no.isdigit(): #datatype check
                    print("Error, number must be in digits.")
                else:
                    valid_resource_no = True
            
            #loop through the loan details to obtain record details
            for record in range(0, len(loan_details)):
                #loop until a match is found
                if loan_details[record][:5] == resource_no:
                    #get and validate evaluation
                    valid_evaluation = False
                    while not valid_evaluation:
                        evaluation = input("Enter evaluation: ")
                        if len(evaluation) == 0: #presence check
                            print("Error, please enter something.")
                        elif not 0 < len(evaluation) <= 50: #length check
                            print("Error, evaluation must not exceed 50 characters.")
                        else:
                            valid_evaluation = True
                            #remove trailing white space
                            loan_details[record] = loan_details[record].rstrip("\n")
                            loan_details[record] = loan_details[record].rstrip(" ")
                            #update the evaluation field
                            loan_details[record] = loan_details[record] + "{0:50s}".format(evaluation)
                            #increment the total number of updates made
                            no_of_updates = no_of_updates + 1
                
            #determine if user wants to enter more input
            valid_option = False
            while not valid_option:
                option = input("Do you wish to return more resources?(Y/N): ")
                option = option.upper()
                if len(option) == 0: #presence check
                    print("Error. Please type something.")
                elif len(option) > 1: #length check
                    print("Error. Please only input 1 character, Y/N.")
                elif not option.isalpha():
                    print("Error. Please input only 1 alphabet.")
                elif not (option == "Y" or option == "N"):
                    print("Error. Input must be either 'Y' or 'N'.")
                else:
                    valid_option = True
                    if option == "N":
                        finish_input = True

        #write updated loan resources to file
        for record in loan_details:
            loan_file.write(record)

        #display the total number of resources returned
        print("Total number of resources returned :", no_of_updates)

    except IOError:
        #output an error if unable to write to file
        print("Error, unable to write to file.")
                
#main
if __name__ == "__main__":
    RETURNRESOURCE()
