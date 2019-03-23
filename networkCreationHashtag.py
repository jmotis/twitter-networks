# begin by extracting Twitter handles from the TAGS spreadsheet
# note: assumes you have downloaded the TAGS spreadsheet from Google Drive and saved archives sheet as a .csv
# you could also programmatically obtain TAGS spreadsheet data via the Sheets API but I wanted to keep it simple

# import modules
import csv

# define function
def extract_handles(file):
    # open and read the files, create Header Row for export .csv
    text = open(file)
    entry = csv.reader(text)

    export_file_name = file[:-4] + "_edge_list.csv"
    handles = open(export_file_name, 'a+')
    handles.write('source,target,hashtag\n')

    # import entities_str column
    for line in entry:
        # extract the initial tweeter handle from column B
        from_user = line[1]
        
        # extract the entities_str (full tweet) text from column Q
        entities_str = line[16]

        # split entities_str into a list whose first item is misc. characters and subsequent items start with a twitter handle
        entities_str = entities_str.split('"screen_name":"')
        
        # remove the first item of misc. characters
        entities_str.pop(0)
        
        # isolate just the twitter handles from subsequent items
        for item in entities_str:
            item = item.split('"')
            item = item[0]
            
            # write initial tweeter handle and entities_str twitter handles to file in network edge format
            handles.write(from_user + ',' + item + ',' + hashtag + '\n')
    
    # close files
    text.close()
    handles.close()
    
# end function definition

#begin program
file_name = input('What is the exact name of your csv file (include the .csv) ')
hashtag = file_name[:-4]
extract_handles(file_name)

# end program