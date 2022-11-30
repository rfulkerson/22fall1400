nums = [7, 6, 1, 4, 9, 3]
f = open('myfile.txt', 'w')
for num in nums:
    f.write(str(num))
f.close()