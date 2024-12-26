import sys
import os

word = "Helloo"

mass = list(word)

registr = dict()
for x in mass:
    if x in registr:
        registr[x] += 1
    else:
        registr[x] = 1
for x in registr:
    if registr[x] > 1:
        print(x)