
def mystery(w):
    a = 0
    v = ['a', 'e', 'i', 'o', 'u']
    for z in range(len(w)):
        if w[z] in v:
            a += 1
    return a

x = mystery("HEllo")
print(x)
x = mystery("Supercalifragilisticexpealidocious")
print(x)