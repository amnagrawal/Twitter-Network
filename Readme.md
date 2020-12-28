OSNA Project: Readme

Project Requirements:
Other than the standard Python Libraries, following two libraries are required to run the project:
 - python-twitter: to collect user information and their followers
 - Networkx: to draw the network and perform graphical operations and retrieve inferences.

Steps to run the project:
 - First run the 'scraper.py' script to get the list of names of users as names.csv
 - Run the 'project.py' script which does the rest of the tasks required to get the reported results

 NOTE: This will take some time to complete the execution of the script as the twitter API limits the rate
 of fetching user information to only 15 requests per 15 minutes. To avoid this, all the required user
 information has been fetched and saved. The saved files are attached with this project. In order to use that:

 - Unpack the project zip file.
 - It should contain 'names.csv' and 'twitter_directed_graph' files along with the python scripts. Make sure
   to save these files in the same directory as the python scripts
 - Simply run the 'project.py' script to use the saved data to get the reported results.