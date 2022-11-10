#highlights from lecture 22

foo = [10,20,30,40,50,20]
print(foo.index(40))
#print(foo.index(5))
print(foo.count(20))
print(foo.count(10))
print(foo.count(5))

phrase = "The quick brown fox jumped over the lazy dog"

print(phrase.split())

person = "Jones,Janie,jjones@placeplaceplace.com"

info = person.split(",")
print(info)
last_name, first_name, email = person.split(",")
print(f"{first_name} {last_name} (email)")

new_string = ":-:".join(info)
print(new_string)

print(phrase)
what = phrase.split(",")
print(what)

foo = [10,20,30,40,50,20]
print(foo)
new_value = int(input("Enter a new value: "))
foo.append(new_value)
print(foo)

print(foo.pop())
print(foo)
foo.pop()
foo.pop()
print(foo)

print(foo.pop(0))
print(foo)

my_list = [1234,1346,451234,1234,2546,1234,2345,1234213265,4]

print(my_list)
my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)