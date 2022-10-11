import random
people = ['Inge', 'Phoenix', "Wei"]
for person in people:
    flip = random.randint(1,2)
    coin = "Heads" if flip == 1 else "Tails"
    print(coin, end=' ')
