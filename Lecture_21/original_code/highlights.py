# highlights from lecture 21

a = "The quick brown fox jumped over the lazy dog"

print(a)
print(a[6])
print(a[10:15])
word = a[10:15]
print(word)
print(a[10:16])
print(a[10:17])

start = 4
stop = 9
print(a[start:stop])


print(a[:15])
print(a[15:])
print(a[0:len(a):5])
print(a[len(a):0:-1])
print(a[::-1])

name = "Robert"
age = 30
name2 = "Bob"
age2 = 135

print("12345678901234567890")
print(name,age)
print(f"{name} {age}")
print(f"{name:10}{age:5}")
print(f"{name2:10}{age2:5}")

print(f"{name:>10}{age:<5}xxxx")
print(f"{name2:>10}{age2:<5}xxxx")

print(a)
a.replace("quick","fleet-footed")
print(a)
b = a.replace("quick","fleet-footed")
print(b)
print(a)
a = a.replace("quick","fleet-footed")
print(a)
