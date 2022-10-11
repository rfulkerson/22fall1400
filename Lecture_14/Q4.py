search = input("Enter a bird: ")
state_birds = {"NE" : "Western Meadowlark", 
   "NM" : "Greater Roadrunner",
   "OK" : "Wild Turkey", "VT" : "Hermit Thrush"}
if search in state_birds:
    print("Found your bird!")
else:
    print("Didn't find your bird!")
