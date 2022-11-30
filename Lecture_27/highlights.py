# highlights from lecture 28
filename = 'data.txt'

# file = open(filename)
# alldata = file.readlines()
# for line in alldata:
#     line = line.strip()
#     print(line)
# file.close()

# file = open(filename,'r')
# for line in file:
#     print(line)
# file.close()

# with open(filename,'r') as file:
#     for line in file:
#         line = line.strip()
#         print(line)
#     print("Hello world!")
#     if 9 == 7:
#         print("Impossible!")

# file = open(filename,'r')
# stuff = file.read()
# print(":::",stuff,":::")
# file.close()
# 
# lines = stuff.split("\n")
# for l in lines:
#     print(l)

# outfile = open("output.txt",'w')
# outfile.write("Already existed? Who cares!")
# outfile.write("Hello world!\n")
# outfile.write("What's up?\n")
# outfile.write("Another line!")
# outfile.close()

# import csv
# with open('courses.csv', 'r') as myfile:
#     csv_reader = csv.reader(myfile)
#     for row in csv_reader:
#         print(f"{row[0]} {row[1]} is {row[2]}")
