import csv


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