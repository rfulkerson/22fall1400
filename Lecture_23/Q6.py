area_codes = [ [308, 402, 531], [319, 515, 563, 641, 712], [316, 620, 785, 913] ]
for row in area_codes: 
    for pos, cell in enumerate(row):
        if pos % 2 == 0:
            print(cell, end=' ')
    print() 