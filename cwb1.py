# Filename: cwb1.py
# Name: Heng U San
# Centre No / Index No: 3024
# Description: Read from RESOURCE.DAT, format data and display to screen

import time #for date formatting

def DISPLAYRESOURCE():
    
    try:
        # open file in read mode
        resource_file = open("RESOURCE.DAT", "r")
        
        # read and process the first line (creation date and number of records)
        heading_line = resource_file.readline()
        heading_line = heading_line.rstrip("\n")
        
        # store creation date and number of records
        creation_date = heading_line[0:10]
        num_records = heading_line[10:]
        
        # display heading with creation date and number of records
        print("Creation date: " + creation_date)
        print("#Resources: " + num_records)
        
        # display subheading for record details
        print("{0:13s}{1:17s}{2:32s}{3:13s}".format("Resource No", "Resource Type", "Title", "Date Acquired"))
        print("-" * 75)
        
        # read record details
        detail_lines = resource_file.readlines()
        
        # loop through the number of records
        for record_line in detail_lines:
            # read and process the record lines
            record_line = record_line.rstrip("\n")
            
            # store resource no, title, date acquired, resource type
            resource_no = record_line[:5]
            title = record_line[5:35]
            date_acquired = record_line[35:41]
            resource_type = record_line[41:]
            
            # format date from DDMMYY to DD-MM-YYYY
            date_acquired = time.strptime(date_acquired, "%d%m%y")
            date_acquired = time.strftime("%d-%m-%Y", date_acquired)
            
            # display formatted record details in required order
            print("{0:13s}{1:17s}{2:32s}{3:13s}".format(resource_no, resource_type, title, date_acquired))

        # close file
        resource_file.close()

    except IOError:
        # display input file error message
        print("Error! Input file does not exist.")

# main
if __name__ == "__main__":
    DISPLAYRESOURCE()
