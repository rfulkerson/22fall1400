w = 15
l = 20
t = 5

if (w * 3 + t > 50) and w > l or w + t > l:
    print('Playoffs')
elif ((w * 3 + t > 30) and w > l) or t > l and w > t:
    print('Midtable')
else:
    print('Relegation')
