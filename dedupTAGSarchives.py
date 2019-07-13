# this is a program to reformat csv data into a readable csv

import csv

# open csv file of places and read stuff

print("WARNING: tweet string IDs are long enough that Excel and other programs truncate them so running this program multiple times may begin running it on the truncated string, resulting in false positives. Double-check your data!")

fileName = input("What is the filename, including .csv? ")
newFileName = fileName[:-4] + "_dedup.csv"

with open(fileName) as csvFile1:
    with open(newFileName, 'w') as csvFile2:
        textReader = csv.reader(csvFile1)
        writeFile = csv.writer(csvFile2)

        # create list of tweet IDs
        tweet_IDs = []

        j = 1

        # loop through rows; if tweet ID is not in list of tweet IDs, add to list and write that row to file; otherwise move on
        for row in textReader:
            if row[0] in tweet_IDs:
                print(row[0] + " is a duplicate")
                j = j + 1
                continue
            else:
                tweet_IDs.append(row[0])
                writeFile.writerow(row)
        #         writeFile.write(row[0])
        #         i = 1
        #         while i < len(row):
        #             writeFile.write("|" + row[i])
        #             i = i + 1
        #         writeFile.write("\n")

        print(str(j) + " duplicate rows found")