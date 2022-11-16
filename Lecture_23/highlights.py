# highlights from lecture 23
# some examples of working with the topics that were covered

temps = [50, 51, 52, 53, 80, 32, 89]
print(temps)
for t in temps:
    print(t)
print("="*10)
for p in range(len(temps)):
    print(temps[p])

grades = [
    [ 60, 60, 70, 98, 97 ],
    [ 67, 68, 78, 86, 78 ],
    [ 67, 68, 80, 86, 78 ],
    ]
print(grades)
for r in range(len(grades)):
    #print(grades[r])
    for c in range(len(grades[r])):
        print(grades[r][c], end='\t')
    print()

print("="*10)
for row_pos,row in enumerate(grades):
    #print(row)
    for col_pos,col in enumerate(row):
        print(col, end='\t')
    print()
    
space = [
        [
            [6,7,8]
            ],
        [
            [6,8,9],
            [10,20,30],
            ]
    
    ]

print(space)

foo = ["Frank","Joe",'Susan',9812,'Allison',"Yasmine"]
print(foo)
print(foo[1:4])
print(foo[1:])
print(foo[:4])
print(foo[1:4:2])
print(foo[1:5:2])
print(foo[1:6:2])
print(foo[1::2])
print(foo[::2])
print(foo[::-1])

# highlights from lecture 25

a = [7, 88, -3]
print(a)
for pos in range(len(a)):
    a[pos] *= 2
print(a)

a = [7, 88, -3]
new_a = [val * 2 for val in a]
print(new_a)
a = [val * 2 for val in a]
print(a)

b = [1234,1,234,1234,]
new_b = ["hello" for value in b]
print(b)
print(new_b)

#c = input().split()
#print(c)
#c = [float(val) for val in c]
#print(c)

#c = input().split()
#for pos in range(len(c)):
#    c[pos] = int(c[pos])


poss_nums = input("enter values: ").split()
print(poss_nums)
poss_nums = [float(val) for val in poss_nums if val.isdecimal() ]
print(poss_nums)

words = input("Enter singular animals: ").split()
print(words)
words = [w + "s" for w in words if "i" in w]
print(words)

#for pos in range(len(words)):
#    words[pos] = words[pos] + "s"
