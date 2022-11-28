pet_ownership = dict(Dog=63.4, Cat=42.7, 
                     Bird=5.7, Fish=5.7)

pet_own = { 'Dog' : 63.4, 'Cat' : 42.7, 'Bird' : 5.7,
            'Fish' : 5.7 }

# options
# print("Option A")
# for pet in pet_ownership.items():
#     print(pet)
# print("Option B")
# for pet, owner in pet_ownership.items():
#     print(pet)
print("Option C")
for pet in pet_ownership.values():
    print(pet)
# print("Option D")    
# for pet in pet_ownership.values():
#     print(pet_ownership[pet])
