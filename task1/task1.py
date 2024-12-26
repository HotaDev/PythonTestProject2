import random

mass = []

for i in range(0, 10):
    mass.append(random.random())

print(max(mass))
print(min(mass)) 
print(sum(mass)/len(mass))
    