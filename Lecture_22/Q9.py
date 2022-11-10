def do_other(v):
   x = v.pop()
   v.insert(1, x)

a = [15, 30, 25, 40]
do_other(a)
print(a)
