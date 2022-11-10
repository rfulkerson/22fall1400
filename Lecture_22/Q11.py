def huh(s):
   s.sort()
   s.pop(-1)
   s.pop(0)

a = [ 6, 1, 2, -1, 5, 1 ]
huh(a)
print(a)