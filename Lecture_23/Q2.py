stuff = input().split(",")
coll = []

for a in stuff:
  if a.strip().isdecimal():
    coll.append(a.strip())

print(coll)
print(sum(coll))
