import csv
from collections import Counter

dental_outlet_list = []
sorted_list = []

with open('warranty_status.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)
	next(csv_reader)

	for line in csv_reader:
		dental_outlet_list.append(line[0])
		counter_list = Counter(dental_outlet_list)

	csv_file.close()

print(counter_list)