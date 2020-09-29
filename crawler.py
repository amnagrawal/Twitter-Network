# importing libraries for beautifulSoup, Regular Expression and CSV
import requests 
import csv
import re
from bs4 import BeautifulSoup 
 
# saving the url for the website from where the names of NFL Players have been extracted 
URL = "https://www.fantasypros.com/nfl/cheatsheets/top-players.php"

r = requests.get(URL) 
#storing the content of the webpage in the soup
soup = BeautifulSoup(r.content, 'html5lib') 
#extracting the div tag where the required information is displayed on the webpage
table = soup.findAll('div', attrs = {'class':'four columns'})
#creating csv file to store the names of the players
csvFile = open("names.csv", 'wt', newline='')
writer = csv.writer(csvFile)

try:
	for i in range (1,4): # using loop because there are 4 columns which store the required info
		for link in table[i].find_all('a', href=True):
			linkname = (link['href'])
			#using regular expression to extract the names of the players from the link
			namesearch = re.search('/nfl/players/(.+?).php', linkname)
			if namesearch:
    				name = namesearch.group(1)
    				name = name.replace("-", " ")
    				#writing the extracted name of the player into the csv file.
    				writer.writerow([name])

finally:
	csvFile.close()
#endOfCode
