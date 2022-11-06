import random

def generate():
    values = []
    for a in range(5):
        v = random.randint(1,5)
        values.append(v)

print(generate())
