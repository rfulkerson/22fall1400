characters = {'Cleric' : {'Armor' : 18, 'Health' : 30,
                'Spells': ['Cure','Guiding Bolt','Sanctuary']},
              'Wizard': {'Armor': 12, 'Health' : 22, 
                'Spells' : ['Magic Missile', 'Sleep', 'Shield']}
}

print(characters['Wizard']['Spells']
)
print(characters['Wizard']['Spells'][2]
)
print(characters['Wizard']['Spells'][1]
)
print(characters['Wizard']['Spells']['Sleep']
)
