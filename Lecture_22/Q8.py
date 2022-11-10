def do_thing(v):
   x = v.pop(0)
   v.append(x)

a = [15, 30, 25]
do_thing(a)
print(a)