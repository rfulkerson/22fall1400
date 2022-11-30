import csv
with open('mycsv.csv', 'r') as myfile:
    csv_reader = csv.reader(myfile)
    for row in csv_reader:
        print(row[0])
