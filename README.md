# twitter-networks
Python 3.x code to create networks from Twitter data collected via Martin Hawksey's TAGS ([Twitter Archiving Google Sheet](https://tags.hawksey.info))

This is code intended to supplement what was originally a manual workflow for collecting and transforming Twitter data into a format amenable for import into network analysis software (specifically, Gephi). TwitterAnalyticsWorkflow.doc is a Word document explaining the original manual workflow, including setting up TAGS for data collection.

The majority of this code is intended to function on TAGS 6.0, including
* networkCreation.py, which automates the transition from TAGS archive sheet to a csv of edges in source/target format.
* networkCreationHashtag.py, which does the same thing as networkCreation.py but also includes the hashtag as a separate column (useful for if you want to combine multiple Twitter networks but maintain information about which hashtag brought each tweet/node into the network. N.B. If the same tweet has multiple hashtags in it, this may cause you to accidentally duplicate that tweet in your final network.)
* fromTAGStoNetworkAnalysis.py, which is a combination of networkCreation.py and networkAnalysis.py. It produces a csv of edges in source/target format as an intermediate step.

Additional code that is not TAGS 6.0-specific includes
* dedupTAGSarchives.py, which deduplicates a spreadsheet based on the first column (Twitter's unique IDs for each tweet) and can be used if you ended up getting duplicate tweets in your dataset for any reason.
* networkAnalysis.py, which calculates some basic network metrics on a source/target list.

For those using TAGS 6.1, the field with the full tweet string is the 17th column instead of the 16th.
If running networkCreation.py leads to the creation of a blank edge list, with just a header row, try networkCreation17.py instead.
If that works fine, you can run all the TAGS 6.0 code by finding the for loop lines where I've set entities_str = line[16] and change it to line[17].