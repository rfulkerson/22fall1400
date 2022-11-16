s = input().split()
f = {}

for a in s:
    if a in f:
        f[a] += 1
    else:
        f[a] = 1

print(f)