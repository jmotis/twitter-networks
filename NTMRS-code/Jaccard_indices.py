# this code is intended to compute the Jaccard index for nodes in a Twitter network (distance between modularity classes from Gephi's algorithms and formally constructed classes)
# it hard codes in information related to a specific Gephi export with 31 modularity classes and 24 formally constructed classes
# note: jaccard_similiarity_score from sklearn.metrics only functions over sets of the same size, which is not the case for our data

import csv

importFile = open("nodes-connected.csv") # hard-coded csv file name
importReader = csv.reader(importFile)	
exportFile = open("JaccardIndices.csv", "w")
exportFile.write("modularity class" + "," + "constructed class" + "," + "modularity class set length" + "," + "constructed class set length" + "," + "intersection length" + "," + "union length" + "," + "jaccard index" + "\r\n")

# initializing index variables and empty lists to iterate through the modularity numbers (0-30) and constructed class numbers (1-24)
mod_i = 0
hood_i = 1 # name is a legacy of first doing this with neighborhoods
temp_i = 0
mod_list = []
hood_list = []

while mod_i < 31: # hard-coded number of modularity classes
    hood_i = 1
    while hood_i < 25:
	
        # construct a list of nodes that have modularity number mod_i and constructed class number hood_i
        for row in importReader:
            if row[21] == str(mod_i): # hard coded row with modularity class number
                list.append(mod_list, row[0]) # hard coded row with Twitter handle
			# calculate the row's constructed class using temporary variables
            if row[3] != "":
                if row[4] != "":
                    if row[5] != "":
                        if row[6] == "library":
                            temp_i = 1
                        elif row[6] == "history":
                            temp_i = 2
                        else:
                            temp_i = 3
                    else:
                        if row[6] == "library":
                            temp_i = 4
                        elif row[6] == "history":
                            temp_i = 5
                        else:
                            temp_i = 6
                else:
                    if row[5] != "":
                        if row[6] == "library":
                            temp_i = 7
                        elif row[6] == "history":
                            temp_i = 8
                        else:
                            temp_i = 9
                    else:
                        if row[6] == "library":
                            temp_i = 10
                        elif row[6] == "history":
                            temp_i = 11
                        else:
                            temp_i = 12
            else:
                if row[4] != "":
                    if row[5] != "":
                        if row[6] == "library":
                            temp_i = 13
                        elif row[6] == "history":
                            temp_i = 14
                        else:
                            temp_i = 15
                    else:
                        if row[6] == "library":
                            temp_i = 16
                        elif row[6] == "history":
                            temp_i = 17
                        else:
                            temp_i = 18
                else:
                    if row[5] != "":
                        if row[6] == "library":
                            temp_i = 19
                        elif row[6] == "history":
                            temp_i = 20
                        else:
                            temp_i = 21
                    else:
                        if row[6] == "library":
                            temp_i = 22
                        elif row[6] == "history":
                            temp_i = 23
                        else:
                            temp_i = 24
                 
			# compare row's constructed class to desired hood_i
            if str(temp_i) == str(hood_i):
                list.append(hood_list, row[0]) # hard coded row with Twitter handle
        print("Just finished modularity class " + str(mod_i) + " and neighborhood " + str(hood_i))
		
        # calculate the Jaccard index and print to exportFile
        intersection_length = len(set(mod_list) & set(hood_list))
        union_length = len(set(mod_list) | set(hood_list))
        if union_length != 0:
            jaccard_index = intersection_length / union_length
        else: #this should never happen but is here for error-checking purposes
            jaccard_index = "nan"
        exportFile.write(str(mod_i) + "," + str(hood_i) + "," + str(len(mod_list)) + "," + str(len(hood_list)) + "," + str(intersection_length) + "," + str(union_length) + "," + str(jaccard_index) + "\r\n")

        # reset variables for next iteration through constructed class numbers
        mod_list = []
        hood_list = []
        temp_i = 0
        hood_i = hood_i + 1
        importFile.seek(0)
        importReader = csv.reader(importFile)
	
    #reset variables for next iteration through modularity numbers
    importFile.seek(0)
    importReader = csv.reader(importFile)
    mod_i = mod_i + 1

# close the files
importFile.close()
exportFile.close()