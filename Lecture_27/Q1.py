f = open('mydata.txt')
lines = f.readlines()
for ln in lines:
    print(ln)

f.close()
    