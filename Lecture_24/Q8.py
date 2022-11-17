def isLeapYear(x):
    result = (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0)
    return result
years = [2004, 2021, 1996, 2003, 2024, 2016, 2000]
leap = [x for x in years if isLeapYear(x)]
print(leap)
