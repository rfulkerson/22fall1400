import csv
values = [[7,4],[1,9]]
with open('newcsv.csv', 'w') as myfile:
    csv_writer = csv.writer(myfile)
    for i in values:
        csv_writer.writerow(sorted(i))
