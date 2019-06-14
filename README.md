# twitter-networks
Code to create networks from Twitter data collected via TAGS 6.0 and some via TAGS 6.1

The complete, manual workflow (including setting up TAGS for data collection) is explained in TwitterAnalyticsWorkflow.doc

For those who wish to analyze the Twitter network in Gephi or another program, the Python script networkCreation.py replaces steps 9-24 in the manual workflow, automating the transition from TAGS archive sheet to a csv of edges in source/target format.
The Python script networkCreationHashtag.py does the same thing only includes the hashtag as a separate column (useful for if you want to combine multiple Twitter networks but maintain information about which hashtag brought each tweet/node into the network. N.B. If the same tweet has multiple hashtags in it, this may cause you to accidentally duplicate that tweet in your final network.)

The Python script networkAnalysis.py partially replaces steps 25 and 26 in the manual workflow, i.e. it calculates some basic network metrics.

The Python script fromTAGStoNetworkAnalysis.py is a combination of both networkCreation.py and networkAnalysis.py. It still produces a csv of edges in source/target format as an intermediate step.

N.B. For TAGS 6.1, the field with the full tweet string is the 17th column instead of the 16th. If running networkCreation.py leads to the creation of a blank edge list, with just a header row, try networkCreation17.py instead.  If that works fine, you can run all the other code by finding the for loop lines where I've set entities_str = line[16] and change it to line[17]