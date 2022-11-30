import csv
grades = {}
with open('mycsv.csv', 'r') as myfile:
    csv_reader = csv.reader(myfile)
    for row in csv_reader:
        grades[row[0]] = row[1] + row[2] + row[3]
print(grades['Padma'])






# myfile = open('mycsv.csv','r')
# csvr = csv.reader(myfile)
# for row in csvr:
#     grades[row[0]] = row[1] + row[2] + row[3]
# print(grades['Padma'])
    
