# twitter-networks
Code to create networks from Twitter data collected via TAGS

The complete, manual workflow (including setting up TAGS for data collection) is explained in TwitterAnalyticsWorkflow.doc

For those who wish to analyze the Twitter network in Gephi or another program, the Python script networkCreation.py replaces steps 9-24 in the manual workflow, automating the transition from TAGS archive sheet to a csv of edges in source/target format.
The Python script networkAnalysis.py partially replaces steps 25 and 26 in the manual workflow, i.e. it calculates some basic network metrics.

The Python script fromTAGStoNetworkAnalysis.py is a combination of both networkCreation.py and networkAnalysis.py. It still produces a csv of edges in source/target format as an intermediate step.