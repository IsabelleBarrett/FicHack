import requests
import re
import csv
from bs4 import BeautifulSoup


csvfile = open('urlsFixed.csv', 'rb')
reader = csv.DictReader(csvfile)
row = next(reader)

print(row.keys())

output = open('urls2.csv', 'wb')
writer = csv.DictWriter(output, row.keys())
writer.writeheader()
writer.writerow(row)

for row in reader:
	print(row["URL"])
	writer.writerow(row)
	payload = {'key1': 'value1', 'key2': 'value2'}
	r = requests.get(row["URL"])
#get html from urls

	soup = BeautifulSoup(r.content, "html.parser")
	result= soup.find("div", {"id": "storytext"})
#parse contents with beautifulsoup and print only the text under "storytext" id
	print result
	if result != None:
		story = result.prettify
		regex = re.compile( '\s*<[^>]+>\s*')
		cleanedStory=regex.sub("\n",str(story))
#cleans output of result.prettify to remove tags

		print cleanedStory