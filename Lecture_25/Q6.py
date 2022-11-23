stuff = input().split()
d = {}
for x in range(0,len(stuff),2):
    d[stuff[x]] = stuff[x+1]

print(d.get('What','Blue'))
print(d.get('25',"Blue"))
