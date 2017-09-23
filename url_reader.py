import csv


csvfile = open('urls.csv', 'rb')
reader = csv.DictReader(csvfile)
row = next(reader)

print(row.keys())

output = open('urls2.csv', 'wb')
writer = csv.DictWriter(output, row.keys())
writer.writeheader()
writer.writerow(row)

for row in reader:
	writer.writerow(row)