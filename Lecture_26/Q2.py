pet_ownership= dict( Reptile=4.5, Dog=63.4,
                     Cat=42.7, Bird=5.7, Fish=5.7 )
for pet, percent in sorted(pet_ownership.items()):
    print(percent, end=' ')
