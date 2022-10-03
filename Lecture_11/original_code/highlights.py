# highlights from lecture 11

father = "John"
mother = "Ella"
daughter = "Analise"
son = "Peter"

daughter = "Ana"

student1 = "John"
student2 = "Ana"
student3 = "Frank"

family = ["John", "Ella", "Analise", "Peter"]
print(family[0])
print(father)
print(f"{family[0]} married {family[1]} and their children are {family[2]} and {family[3]}.")

random_data = ["anything", 3.14, "of", 34, "any type"]

family.append("Zena")
family.append("Ginny")
family.append("Gabby")

print(family.index("Peter"))
print(family)
family.pop()
family.pop()
store = family.pop()
print(store)
print(family)

temperatures = [70, 72, 68, 68, 50, 60]
print(temperatures)
print(max(temperatures))
print(min(temperatures))
print(sum(temperatures))
print(temperatures.index(max(temperatures)))

#print(max(random_data))

print(max(family))
print(min(family))

family_tuple = ("John", "Ella", "Analise", "Peter")
print(family_tuple[0])
print(f"{family_tuple[0]} married {family_tuple[1]} and their children are {family_tuple[2]} and {family_tuple[3]}.")

family_tuple[0] = "Jack"
