f = open('mydata.txt')
stuff = f.read()
lines = stuff.split("\n")
for ln in lines:
    print(ln)
f.close()