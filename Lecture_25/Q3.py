names = []
n = input("Enter name: ")
while n != "done":
    names.append(n)
    n = input("Enter name: ")
names.sort(reverse=True)
print(names)
