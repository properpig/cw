# Filename: cwb3.py
# Name: Heng U San
# Centre No / Index No: 3024
# Description: Read from LOAN.DAT

import datetime
import time

def CREATELOAN():
    
    try:
        #Open updated resource file for reading
        uresource_file = open("URESOURCE.DAT", "r")
        
        #Read and skip first line
        heading_line = uresource_file.readline()
        
        #Read record details
        detail_lines = uresource_file.readlines()
        
        #Initialize resource number list
        resource_no_list =[]
        
        #Loop through each record
        for resource_line in detail_lines:
            
            #Slice to get resource number
            resource_no = resource_line[0:5]
            
            #Append resource number to resource number list
            resource_no_list.append(resource_no)
            
        #Open loan file for appending
        loan_file = open("LOAN.DAT", "a")

        #Initialize a list of
        on_loan_resource_no_list = []
        student_id_list = []

        #Run a loop until user is done with input
        finish_input = False
        while not finish_input:
            #Get and validate resource number
            valid_resource_no = False
            while not valid_resource_no:
                new_resource_no = input("Enter resource number: ")
                if len(new_resource_no) == 0: #presence check
                    print("Error. Please enter something.")
                elif len(new_resource_no) != 5: #length check
                    print("Error, resource number must be exactly 5 characters.")
                elif not new_resource_no.isdigit(): #datatype check
                    print("Error, number must be in digits.")
                elif new_resource_no not in resource_no_list: #check that resource number exists
                    print("Error, resource number does not exist, please check input.")
                elif new_resource_no in on_loan_resource_no_list: #check that resource is currently available
                    print("Error, this resource is already on loan, please check input.")
                else:
                    valid_resource_no = True
                    
            #Get and validate student ID
            valid_student_ID = False
            while not valid_student_ID:
                student_id = input("Enter student ID: ")
                if len(student_id) == 0: #presence check
                    print("Error. Please enter something.")
                elif len(student_id) != 5: #length check
                    print("Error, student ID must be exactly 5 characters.")
                elif student_id[0] != 'S': #datatype check for first character
                    print("Error, first character must be 'S'.")
                elif not student_id[1:5].isdigit(): #datatype check for last 4 characters
                    print("Error, the last 4 characters must be digits.")
                elif not (0000 < int(student_id[1:5]) <= 9999): #range check
                    print("Error, student ID must be between S0001 - S9999.")
                elif student_id_list.count(student_id) == 3:
                    print("Error. Student has already borrowed the maximum of 3 resources.")

                else:
                    valid_student_ID = True
                    
            #Get and validate student name
            valid_student_name = False
            while not valid_student_name:
                student_name = input("Enter student name: ")
                if len(student_name) == 0: #presence check
                    print("Error. Please enter something.")
                elif len(student_name) > 30: #length check
                    print("Error, student name cannot exceed 30 characters.")
                else:
                    valid_student_name = True

            #Get evaluation
            evaluation = ""
                
            #Calculate and display date due back
            date_due_back = datetime.date.today() + datetime.timedelta(7)
            print("Date due back: " + date_due_back.strftime("%d-%m-%Y"))
        
            #Write valid records into file
            loan_file.write("{0:5}{1:5}{2:30}{3:6}{4:50}".format(new_resource_no, student_id, student_name, date_due_back.strftime("%d%m%y"), evaluation) + "\n")

            #Update on loan resource number list
            on_loan_resource_no_list.append(new_resource_no)

            #Update student id list
            student_id_list.append(student_id)

            #Write valid records into file
            loan_file.write("{0:5}{1:5}{2:30}{3:6}{4:50}".format(new_resource_no, student_id, student_name, date_due_back.strftime("%d%m%y"), evaluation) + "\n")
                        
            #Ask if user wishes to enter more input
            valid_option = False
            while not valid_option:
                option = input("Do you wish to enter a new loan record?(Y/N): ")
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
            
        #Close files
        loan_file.close()
        uresource_file.close()     

    except IOError:
        #Display file input and output error
        print("Error! Cannot read from input file or write to output file.")

#main
if __name__ == "__main__":
    CREATELOAN()
