from math import factorial
from random import shuffle
from copy import deepcopy

vowels = ["a","e","i","o","u","y","ä"]
Options = factorial(len(vowels))
Possibilities = []
while len(Possibilities) < Options:
    if vowels not in Possibilities:
        Possibilities.append(deepcopy(vowels))
    else:
        shuffle(vowels)

print(Possibilities)