# highlights from lecture 25

stuff = { "this" : 1, "that" : 2, "theother" : 3 }

print(stuff)
print(stuff["this"])
#print(stuff["thing"])

if "thing" in stuff:
    print(stuff["thing"])
else:
    print("thing isn't in the dictionary!")

print(stuff.get("thing","thing isn't in the dictionary"))
print(stuff.get("that","that isn't in the dictionary"))
print(stuff.get("whatever",""))
print("after")

remember = stuff.get("that","")
storage = stuff.get("whatever","")

print(remember,storage,"after")




    
