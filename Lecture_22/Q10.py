def function(y):
    thing = 0
    if "e" in y or "a" in y:
        thing = y.count('a')
    return thing

z = ["abba", "you", "e", "a", "t"]
print(function(z))
