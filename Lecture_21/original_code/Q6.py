phrase = "There's a lady who's sure all that glitters is gold"
search = "gold"

#if phrase contains search:
#    print("Found it!")
if search in phrase:
    print("Found it1!")
if search == phrase:
    print("Found it2!")
if search.find(phrase) >= 0:
    print("Found it3!")
