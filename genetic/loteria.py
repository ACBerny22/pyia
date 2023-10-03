import random

baraja = []

for i in range(16):
    selection = random.randint(1, 54)
    baraja.append(selection)

print(baraja)