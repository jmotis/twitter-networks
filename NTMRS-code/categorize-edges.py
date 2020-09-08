# this code is intended to categorize edges in a node list as "within-discipline" or "cross-disciplines/interdisciplinary"
# it hard codes in information for spreadsheets and makes assumptions about spreadsheet formatting

import csv

importFile = open("book-edges.csv") # hard-coded csv file name
importReader = csv.reader(importFile)
classifyFile = open("classified-nodes.csv") # hard-coded csv file name
classifyReader = csv.reader(classifyFile)
exportFile = open("classified-edges.csv", "w")
exportFile.write("Source,Target,Weight,Source-Affiliation,Target-Affiliation,Categorization\r\n")

# initializing index variables and empty lists to iterate through the modularity numbers (0-30) and constructed class numbers (1-24)
source = ""
target = ""
discipline = ""

# iterate through cl
for edgeRow in importReader:
    if edgeRow == "Id":
        continue
    else:    
        for nodeRow in classifyReader:
            if edgeRow[0] == nodeRow[0]:
                source = nodeRow[4]
            if edgeRow[1] == nodeRow[0]:
                target = nodeRow[4]
        if source == target:
            discipline = "in"
        else:
            discipline = "out"
        exportFile.write(edgeRow[0] + "," + edgeRow[1] + "," + edgeRow[2] + "," + source + "," + target + "," + discipline + "\r\n")
        print(edgeRow)
        print ("is done!")
        
    # reset variables for next iteration
    classifyFile.seek(0)
    classifyReader = csv.reader(classifyFile)
    source = ""
    target = ""
    discipline = ""

# close the files
importFile.close()
classifyFile.close()
exportFile.close()